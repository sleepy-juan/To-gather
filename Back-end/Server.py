# Server.py
# - To-gather Server Program
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)
# Author @ Sungwoo Jeon (j0070ak@kaist.ac.kr)
import socket
from System import fork, lock, wait, alarm, repeat, cancel
from Packet import OnThrow
import random

class Server:
	LISTENQ = 1024

	def __init__(self, PORT):
		self.sock = socket.socket()
		self.sock.bind(('', PORT))
		self.sock.listen(Server.LISTENQ)
		self.clients = {}
		self.answer_queue = {}

		def accept_handler(argument):
			sock, clients, handler, queue = argument
			while True:
				client, address = sock.accept()
				username = client.recv(64).strip().decode()

				with lock():
					clients[username] = client
					if username not in queue:
						queue[username] = []

				print('accept', username)

				fork(handler, (client, username))

		fork(accept_handler, (self.sock, self.clients, self.per_clients, self.answer_queue))

	def close(self):
		self.sock.close()
		for key in self.clients:
			self.clients[key].close()

	def per_clients(self, arg):
		sock, username = arg
		answer_queue = self.answer_queue
		clients = self.clients

		while True:
			try:
				Type = sock.recv(4).decode()
			except:
				Type = "QUIT"

####################################################################
			if Type == "QUIT":
				with lock():
					del self.clients[username]
				break
####################################################################
			elif Type == "THRW":
				q = OnThrow(sock)

				print('recv', q.questioner)
				print('recv', q.question)
				for a in q.answers:
					print('recv', a.answerer)
					print('recv', a.answer)

				passed_answerers = list(map(lambda x:x.answerer, q.answers))
				valid_answerers = list(filter(lambda x: (x not in passed_answerers) and (x != username), clients.keys()))

				if len(valid_answerers) == 0:
					sock.send("EMTY".encode())
					continue

				answerer = random.choice(valid_answerers)
				with lock():
					answer_queue[answerer].append(q)
				sock.send("DONE".encode())
####################################################################
			elif Type == "RECV":
				#to do something'
				pass
####################################################################
			elif Type == "CNFM":
				pass
####################################################################
			elif Type == "CHCK":
				pass
####################################################################
			elif Type == "ENDS":
				pass