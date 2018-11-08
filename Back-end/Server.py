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
		self.timers = []

		def accept_handler(argument):
			sock, clients, handler, answer_queue, confirm_queue, timers = argument
			while True:
				client, address = sock.accept()
				username = RecvFormat(client)

				with lock():
					clients[username] = client
					if username not in answer_queue:
						answer_queue[username] = []
					if username not in confirm_queue:
						confirm_queue[username] = []
				fork(handler, (client, username))

		fork(accept_handler, (self.sock, self.clients, self.per_clients, self.answer_queue, self.confirm_queue, self.timers))

		def timeout_handler(argument):
			timers = argument

			while True:
				curtime = time.time()
				handling = []

				with lock():
					for timer in timers:
						if curtime - timer[2] > Protocol.INTS.TIME_OUT_IN_SECONDS:
							handling.append(timer)
							timers.remove(timer)

				for handle in handling:
					answers = Database.getAnswer(handle[1])
					question = Database.getQuestion(handle[1])
					passed_answerers = list(map(lambda x:x.questioner, answers))
					valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != question.questioner) and (x != handle[0]), clients.keys()))

					if len(valid_answerers) == 0:
						with lock():
							self.confirm_queue[question.questioner].append(handle[1])
						continue

					answerer = random.choice(valid_answerers)
					with lock():
						answer_queue[answerer].append(handle[1])
						timers.append((answerer, handle[1], curtime))

		fork(timeout_handler, self.timers)

	def close(self):
		self.sock.close()
		for key in self.clients:
			self.clients[key].close()

	def per_clients(self, arg):
		sock, username = arg
		answer_queue = self.answer_queue
		confirm_queue = self.confirm_queue
		clients = self.clients
		timers = self.timers

		while True:
			try:
				command = sock.recv(4).decode()
			except:
				command = Protocol.CLIENT.QUIT

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
					sock.send(Protocol.SERVER.NO_AVAILABLE_USER.encode())
					continue

				answerer = random.choice(valid_answerers)
				try:
					with lock():
						Database.logQuestion(question)
						answer_queue[answerer].append(question.front_id)
						timers.append((answerer, question.front_id, time.time()))
				except:
					sock.send(Protocol.SERVER.NO_AVAILABLE_USER.encode())
				sock.send(Protocol.SERVER.SUCCESS.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_QUESTIONS:
				SendIds(sock, answer_queue[username])
				sock.send(Protocol.SERVER.SUCCESS.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_QUESTION:
				qid = sock.recv(64).strip().decode()
				question = Database.getQuestion(qid)
				if question == None:
					SendEmptyFormat(sock)
					sock.send(Protocol.SERVER.TIMED_OUT)
					continue

				SendFormat(question)
				sock.send(Protocol.SERVER.SUCCESS.encode())
####################################################################
			elif command == Protocol.CLIENT.ANSWER:
				answer = RecvFormat(sock)
				try:
					with lock():
						answer_queue[username].remove(answer.front_id)
				except:
					sock.send(Protocol.SERVER.TIMED_OUT.encode())

				Database.logAnswer(answer)
				try:
					with lock():
						confirm_queue[answer.questioner].append(answer.front_id)
				except:
					sock.send(Protocol.SERVER.NO_AVAILABLE_USER.encode())
				sock.send(Protocol.SERVER.SUCCESS.encode())
####################################################################
			elif command == Protocol.CLIENT.GET_CONFIRMS:
				SendIds(sock, confirm_queue[username])
				sock.send(Protocol.SERVER.SUCCESS.encode())
####################################################################
			elif command = Protocol.CLIENT.CONFIRM_ENDS:
				qid = sock.recv(64).strip().decode()
				try:
					with lock():
						confirm_queue[username].remove(qid)
				except:
					sock.send(Protocol.SERVER.WRONG_CONFIRMATION.encode())
				sock.send(Protocol.SERVER.SUCCESS.encode())
####################################################################
			else:
				pass