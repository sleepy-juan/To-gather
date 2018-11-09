# Server.py
# - To-gather Server Program
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)
# Editor @ Sungwoo Jeon (j0070ak@kaist.ac.kr)
import socket
from System import fork, lock, wait, alarm, repeat, cancel
from Packet import *
import random
from Disk import Database
import time

from Constants import Protocol

class Server:
	LISTENQ = 1024

	def __init__(self, PORT):
		self.sock = socket.socket()
		self.sock.bind(('', PORT))
		self.sock.listen(Server.LISTENQ)
		self.clients = {}
		self.answer_queue = {}
		self.confirm_queue = {}
		self.delayed_queue = {}
		self.timers = []

		def accept_handler(argument):
			sock, clients, handler, answer_queue, confirm_queue, delayed_queue, timers = argument
			while True:
				client, address = sock.accept()
				username = RecvUsername(client)

				print("[SYSTEM] %s connected from (IP: %s, PORT: %d)" % (username, address[0], address[1]))

				with lock():
					clients[username] = client
					if username not in answer_queue:
						answer_queue[username] = []
					if username not in confirm_queue:
						confirm_queue[username] = []
					if username not in delayed_queue:
						delayed_queue[username] = []
				fork(handler, (client, username))

		fork(accept_handler, (self.sock, self.clients, self.per_clients, self.answer_queue, self.confirm_queue, self.delayed_queue, self.timers))

		def timeout_handler(argument):
			print("[TIMER] Called")
			timers = argument
			curtime = time.time()
			handling = []

			with lock():
				for timer in timers:
					if curtime - timer[2] > Protocol.INTS.TIME_OUT_IN_SECONDS:
						handling.append(timer)
						timers.remove(timer)
						self.answer_queue[timer[0]].remove(timer[1])

				for user in self.delayed_queue:
					for qid in self.delayed_queue[user]:
						handling.append((user, qid, 0))	# force to handle
					self.delayed_queue[user].clear()

			print(handling)
			for handle in handling:
				answers = Database.getAnswer(handle[1])
				question = Database.getQuestion(handle[1])
				passed_answerers = list(map(lambda x:x.questioner, answers))

				# TODO:
				# 메시지 하나가 자꾸 delayed queue에 멈춰있음.
				# 해결할 필요 !!!!
				# 위에 있는 list 들 출력해서 결과 확인해보면 될듯.

				with lock():
					valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != question.questioner) and (x != handle[0]), self.clients.keys()))

				if len(valid_answerers) == 0:
					if handle[2] == 0:
						with lock():
							self.delayed_queue[handle[0]].append(handle[1])
					else:
						with lock():
							self.delayed_queue[question.questioner].append(handle[1])
					continue

				answerer = random.choice(valid_answerers)
				with lock():
					print("[TIMER] time out! id %s moved from %s to %s" % (handle[1], handle[0], answerer))
					self.answer_queue[answerer].append(handle[1])
					timers.append((answerer, handle[1], curtime))


		repeat(timeout_handler, 10, self.timers)

	def close(self):
		self.sock.close()
		for key in self.clients:
			self.clients[key].close()

	def per_clients(self, arg):
		sock, username = arg
		answer_queue = self.answer_queue
		confirm_queue = self.confirm_queue
		delayed_queue = self.delayed_queue
		clients = self.clients
		timers = self.timers

		while True:
			try:
				command = sock.recv(4).decode()
			except:
				command = Protocol.CLIENT.QUIT

			if command == '':
				command = Protocol.CLIENT.QUIT

			print("[%s] Received command %s" % (username, command))

####################################################################
			if command == Protocol.CLIENT.QUIT:
				try:
					with lock():
						del self.clients[username]
				except:
					pass

				break
####################################################################
			elif command == Protocol.CLIENT.POST_QUESTION:
				question = RecvFormat(sock)

				answers = Database.getAnswer(question.front_id)
				passed_answerers = list(map(lambda x:x.questioner, answers))
				valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != username), clients.keys()))

				if len(valid_answerers) == 0:
					print("[SYSTEM] No Valid Answerers")
					with lock():
						Database.logQuestion(question)
						delayed_queue[username].append(question.front_id)
					sock.send(Protocol.SERVER.NO_AVAILABLE_USER.encode())
					continue

				answerer = random.choice(valid_answerers)

				check = True
				with lock():
					try:
						Database.logQuestion(question)
					except Exception as e:
						print("[SYSTEM] Database Error: cannot log question")
						print(e)
						check = False
					try:
						answer_queue[answerer].append(question.front_id)
					except Exception as e:
						print("[SYSTEM] Answer Queue of %s is not set" % answerer)
						print(e)
						check = False
					try:
						timers.append((answerer, question.front_id, time.time()))
					except:
						print("[SYSTEM] Timer set failed")
						check = False

				if not check:
					sock.send(Protocol.SERVER.NO_AVAILABLE_USER.encode())
				else:
					sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_QUESTIONS:
				SendIds(sock, answer_queue[username])
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_QUESTION:
				qid = sock.recv(64).strip().decode()
				if qid not in answer_queue[username] and qid not in confirm_queue[username]:
					SendEmptyFormat(sock)
					print("[SYSTEM] id %s not in %s's answer queue" % (qid, username))
					sock.send(Protocol.SERVER.TIMED_OUT.encode())
					continue

				question = Database.getQuestion(qid)
				SendFormat(sock, question)
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.ANSWER:
				answer = RecvFormat(sock)
				try:
					with lock():
						answer_queue[username].remove(answer.front_id)
						for timer in timers:
							if timer[0] == username and timer[1] == answer.front_id:
								timers.remove(timer)
								break
				except:
					print("[SYSTEM] id %s not in %s's answer queue" % (answer.front_id, username))
					sock.send(Protocol.SERVER.TIMED_OUT.encode())

				Database.logAnswer(answer)
				question = Database.getQuestion(answer.front_id)
				try:
					with lock():
						print("[SYSTEM] ASK confirm of %s to %s" % (answer.front_id, question.questioner))
						confirm_queue[question.questioner].append(answer.front_id)
				except:
					print("[SYSTEM] %s is not available" % question.questioner)
					sock.send(Protocol.SERVER.NO_AVAILABLE_USER.encode())
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_CONFIRMS:
				SendIds(sock, confirm_queue[username])
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_ANSWERS:
				qid = sock.recv(64).strip().decode()
				answers = Database.getAnswer(qid)
				SendManyFormat(sock, answers)
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.CONFIRM_ENDS:
				qid = sock.recv(64).strip().decode()
				try:
					with lock():
						confirm_queue[username].remove(qid)
				except:
					sock.send(Protocol.SERVER.WRONG_CONFIRMATION.encode())
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			else:
				pass