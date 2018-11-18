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
from Common import common

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
		self.clients = []
<<<<<<< HEAD
		self.user_info = {}
		self.questions = []
=======
		self.questions = Database.getOnQuestions()
>>>>>>> a0f170f1d3be8d2740d86b93926d6aa2de448793

		def accept_handler(argument):
			sock, clients, handler = argument
			while True:
				client, address = sock.accept()

				fork(handler, client)

		fork(accept_handler, (self.sock, self.clients, self.per_clients))

		def timeout_handler(argument):
			questions = argument
			curtime = time.time()

			with lock():
				for question in questions:
					if question.status == Status.QUESTION.DELAYED:
						answers = Database.getAnswer(question.qid)
						passed_answerers = list(map(lambda x:x.questioner, answers))
						valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != question.belong_to) and (x != question.sent_from), self.clients))

						if len(valid_answerers) == 0:
							print("Current Users:", self.clients)
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
						valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != question.belong_to) and (x != question.sent_from), self.clients))

						if len(valid_answerers) == 0:
							question.status = Status.QUESTION.ON_CONFIRM
							question.belong_to = question.sent_from
							question.created = time.time()
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
		Database.logOnQuestions(self.questions)

	def per_clients(self, arg):
		sock = arg
		questions = self.questions
		clients = self.clients

		username, command, body = GetHTTP(sock)

		username = username.strip()
		if username == '':
			ResponseHTTP(sock, Protocol.SERVER.WRONG_COMMAND)
			return

		if command not in [ \
			Protocol.CLIENT.GET_QUESTIONS,
			Protocol.CLIENT.GET_QUESTION,
			Protocol.CLIENT.GET_CONFIRMS,
			Protocol.CLIENT.GET_PUBLICS,
			Protocol.CLIENT.GET_OWNS,
			Protocol.CLIENT.GET_PUBLICS,
		]:
			print("[%s] Received command %s" % (username, command))

		with lock():
			if username not in clients:
				clients.append(username)
				print("[SYSTEM] %s joins to server" % username)
			if username not in user_info:
				user_info[username] = Common()

####################################################################
		if command == Protocol.CLIENT.QUIT:
			with lock():
				if username in self.clients:
					clients.remove(username)
			ResponseHTTP(sock, Protocol.SERVER.OK)
####################################################################
		elif command == Protocol.CLIENT.POST_QUESTION:
			question = RecvFormat(body)
			print('question: ' + question.comment_text)

			check = Database.getQuestion(question.front_id)
			if check != None:
				print("[%s] id is duplicated" % username)
				ResponseHTTP(sock, Protocol.SERVER.DUPLICATED_QUESTION)
				return

			answers = Database.getAnswer(question.front_id)
			passed_answerers = list(map(lambda x:x.questioner, answers))
			with lock():
				valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != username), clients))

			Database.logQuestion(question)

			if len(valid_answerers) == 0:
				print("[%s] No Valid Answerers" % username)
				with lock():
					questions.append(Server._SimpleQuestion(question.front_id, username, username, Status.QUESTION.DELAYED, time.time()))
				ResponseHTTP(sock, Protocol.SERVER.NO_AVAILABLE_USER)
				return

			answerer = random.choice(valid_answerers)
			with lock():
				questions.append(Server._SimpleQuestion(question.front_id, username, answerer, Status.QUESTION.SENT, time.time()))
			ResponseHTTP(sock, Protocol.SERVER.OK)
####################################################################
		elif command == Protocol.CLIENT.GET_QUESTIONS:
			ids = []
			with lock():
				for question in questions:
					if question.belong_to == username and question.status == Status.QUESTION.SENT:
						ids.append(question.qid)
			ResponseHTTP(sock, Protocol.SERVER.OK, '\n'.join(ids))
####################################################################
		elif command == Protocol.CLIENT.GET_QUESTION:
			qid = body
			question = Database.getQuestion(qid)
			if Database.howManyHelp(question.questioner,username) == 0:
				question.content_common = user_common(user_info, username, question.questioner)
			else:
				question.content_common = 'help' + str(Database.howManyHelp(question.questioner, username))
			ResponseHTTP(sock, Protocol.SERVER.OK, SendFormat(question))
####################################################################
		elif command == Protocol.CLIENT.ANSWER:
			answer = RecvFormat(body)
			Database.logAnswer(answer)
			question = Database.getQuestion(answer.front_id)
			Database.logHelp(username, question.questioner)
			print("answer: " + answer.comment_text)
			with lock():
				for question in questions:
					if question.qid == answer.front_id:
						question.status = Status.QUESTION.ON_CONFIRM
						question.belong_to = question.sent_from
			ResponseHTTP(sock, Protocol.SERVER.OK)
####################################################################
		elif command == Protocol.CLIENT.GET_CONFIRMS:
			ids = []
			with lock():
				for question in questions:
					if question.belong_to == username and question.status == Status.QUESTION.ON_CONFIRM:
						ids.append(question.qid)
			ResponseHTTP(sock, Protocol.SERVER.OK, '\n'.join(ids))
####################################################################
		elif command == Protocol.CLIENT.GET_PUBLICS:
			ids = Database.getAllIDs()
			with lock():
				for question in questions:
					try:
						ids.remove(question.qid)
					except:
						pass
			ResponseHTTP(sock, Protocol.SERVER.OK, '\n'.join(ids))
####################################################################
		elif command == Protocol.CLIENT.GET_OWNS:
			ids = Database.getAllIDs()
			with lock():
				for question in questions:
					if question.belong_to == username: continue
					try:
						ides.remove(question.qid)
					except:
						pass
			ResponseHTTP(sock, Protocol.SERVER.OK, '\n'.join(ids))
####################################################################
		elif command == Protocol.CLIENT.GET_ANSWERS:
			qid = body
			ResponseHTTP(sock, Protocol.SERVER.OK, SendManyFormat(Database.getAnswer(qid)))
####################################################################
		elif command == Protocol.CLIENT.CONFIRM_ENDS:
			qid = body
			with lock():
				for question in questions:
					if question.qid == qid:
						questions.remove(question)
			ResponseHTTP(sock, Protocol.SERVER.OK)
####################################################################
		elif command == Protocol.CLIENT.CONTINUE_QUESTION:
			qid = body
			with lock():
				for question in questions:
					if question.qid == qid:
						answers = Database.getAnswer(qid)
						passed_answerers = list(map(lambda x:x.questioner, answers))
						valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != question.sent_from), clients))

						if len(valid_answerers) == 0:
							print("[%s] No Valid Answerers" % username)
							ResponseHTTP(sock, Protocol.SERVER.NO_AVAILABLE_USER)
							return

						answerer = random.choice(valid_answerers)
						question.status = Status.QUESTION.SENT
						question.belong_to = answerer
						question.created = time.time()
						ResponseHTTP(sock, Protocol.SERVER.OK)
						return
			ResponseHTTP(sock, Protocol.SERVER.WRONG_COMMAND)
####################################################################
		elif command == Protocol.CLIENT.LIST_MEMBERS:
			with lock():
				ResponseHTTP(sock, Protocol.SERVER.OK, '\n'.join(clients))
####################################################################
		else:
			ResponseHTTP(sock, Protocol.SERVER.WRONG_COMMAND)