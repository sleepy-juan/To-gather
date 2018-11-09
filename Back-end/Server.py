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

from Constants import Protocol, Status

class Server:
	LISTENQ = 1024

	class _SimpleQuestion:
		def __init__(self, qid, sent_from, belong_to, status, created):
			self.qid = qid
			self.sent_from = sent_from
			self.belong_to = belong_to
			self.status = status
			self.created = created

	def __init__(self, PORT):
		self.sock = socket.socket()
		self.sock.bind(('', PORT))
		self.sock.listen(Server.LISTENQ)
		self.clients = {}
		self.questions = []
		self.timers = []

		def accept_handler(argument):
			sock, clients, handler, questions, timers = argument
			while True:
				client, address = sock.accept()
				username = RecvUsername(client)

				print("[SYSTEM] %s connected from (IP: %s, PORT: %d)" % (username, address[0], address[1]))

				with lock():
					clients[username] = client
				fork(handler, (client, username))

		fork(accept_handler, (self.sock, self.clients, self.per_clients, self.questions, self.timers))

		def timeout_handler(argument):
			print("[TIMER] Called")
			questions = argument
			curtime = time.time()

			with lock():
				for question in questions:
					if question.status == Status.QUESTION.DELAYED:
						answers = Database.getAnswer(question.qid)
						passed_answerers = list(map(lambda x:x.questioner, answers))
						valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != question.belong_to), self.clients.keys()))

						if len(valid_answerers) == 0:
							print("Current Users:", self.clients.keys())
							print("Passed Users:", passed_answerers)
							print("Belong To:", question.belong_to)
							print("[TIMER] delayed but still no valid answerers")
							continue

						answerer = random.choice(valid_answerers)
						print("[TIMER] delayed now valid! from %s to %s" % (question.belong_to, answerer))
						question.status = Status.QUESTION.SENT
						question.created = time.time()
						question.belong_to = answerer

					elif curtime - question.created > Protocol.INTS.TIME_OUT_IN_SECONDS:
						answers = Database.getAnswer(question.qid)
						passed_answerers = list(map(lambda x:x.questioner, answers))
						valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != question.belong_to), self.clients.keys()))

						if len(valid_answerers) == 0:
							question.status = Status.QUESTION.ON_CONFIRM
							question.belong_to = question.sent_from
							print("[TIMER] timeout'd but no valid answerer -> confirm")
							continue

						answerer = random.choice(valid_answerers)
						print("[TIMER] delayed now valid! from %s to %s" % (question.belong_to, answerer))
						question.status = Status.QUESTION.SENT
						question.created = time.time()
						question.belong_to = answerer

		repeat(timeout_handler, 10, self.questions)

	def close(self):
		self.sock.close()
		for key in self.clients:
			self.clients[key].close()

	def per_clients(self, arg):
		sock, username = arg
		questions = self.questions
		clients = self.clients

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
				check = Database.getQuestion(question.front_id)
				if check != None:
					print("[%s] id is duplicated" % username)
					sock.send(Protocol.SERVER.DUPLICATED_QUESTION.encode())
					continue

				answers = Database.getAnswer(question.front_id)
				passed_answerers = list(map(lambda x:x.questioner, answers))
				with lock():
					valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != username), clients.keys()))

				Database.logQuestion(question)

				if len(valid_answerers) == 0:
					print("[%s] No Valid Answerers" % username)
					with lock():
						questions.append(Server._SimpleQuestion(question.front_id, username, username, Status.QUESTION.DELAYED, time.time()))
					sock.send(Protocol.SERVER.NO_AVAILABLE_USER.encode())
					continue

				answerer = random.choice(valid_answerers)
				with lock():
					questions.append(Server._SimpleQuestion(question.front_id, username, answerer, Status.QUESTION.SENT, time.time()))
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_QUESTIONS:
				ids = []
				with lock():
					for question in questions:
						if question.belong_to == username and question.status == Status.QUESTION.SENT:
							ids.append(question.qid)
				SendIds(sock, ids)
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_QUESTION:
				qid = sock.recv(64).strip().decode()
				with lock():
					for question in questions:
						if question.qid == qid and question.belong_to == username:
							SendFormat(sock, Database.getQuestion(qid))
							sock.send(Protocol.SERVER.OK.encode())
							break
					else:
						SendEmptyFormat(sock)
						print("[%s] id %s not in %s's answer queue" % (username, qid, username))
						sock.send(Protocol.SERVER.TIMED_OUT.encode())
####################################################################
			elif command == Protocol.CLIENT.ANSWER:
				answer = RecvFormat(sock)
				Database.logAnswer(answer)
				with lock():
					for question in questions:
						if question.qid == answer.front_id:
							question.status = Status.QUESTION.ON_CONFIRM
							question.belong_to = question.sent_from
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_CONFIRMS:
				ids = []
				with lock():
					for question in questions:
						if question.belong_to == username and question.status == Status.QUESTION.ON_CONFIRM:
							ids.append(question.qid)
				SendIds(sock, ids)
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
				with lock():
					for question in questions:
						if question.qid == qid:
							questions.remove(question)
				sock.send(Protocol.SERVER.OK.encode())
####################################################################
			else:
				pass