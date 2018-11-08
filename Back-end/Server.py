# Server.py
# - To-gather Server Program
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)
# Author @ Sungwoo Jeon (j0070ak@kaist.ac.kr)
import socket
from System import fork, lock, wait, alarm, repeat, cancel
from Packet import OnThrow, OnAccept, OnRelay
import random
from Disk import Database

class Server:
	LISTENQ = 1024

	def __init__(self, PORT):
		self.sock = socket.socket()
		self.sock.bind(('', PORT))
		self.sock.listen(Server.LISTENQ)
		self.clients = {}
		self.answer_queue = {}
		self.confirm_queue = {}

		def accept_handler(argument):
			sock, clients, handler, answer_queue, confirm_queue = argument
			while True:
				client, address = sock.accept()
				username, location = OnAccept(client)

				Database.logLocation(username, location)

				with lock():
					clients[username] = client
					if username not in answer_queue:
						answer_queue[username] = []
					if username not in confirm_queue:
						confirm_queue[username] = []
				fork(handler, (client, username))

		fork(accept_handler, (self.sock, self.clients, self.per_clients, self.answer_queue, self.confirm_queue))

	def close(self):
		self.sock.close()
		for key in self.clients:
			self.clients[key].close()

	def per_clients(self, arg):
		sock, username = arg
		answer_queue = self.answer_queue
		confirm_queue = self.confirm_queue
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
			elif Type == "RELY":
				with lock():
					OnRelay(sock, answer_queue[username])
				sock.send("DONE".encode())
####################################################################
			elif Type == "ANSW":
				q = OnThrow(sock)
				with lock():
					for i in range(answer_queue[username]):
						if q.id == i.id:
							answer_queue[username].remove(i)
							break
				confirm_queue[q.questioner].append(q)
				sock.send("DONE".encode())
####################################################################
			elif Type == "CNFM":
				with lock():
					OnRelay(sock, confirm_queue[username])
					del confirm_queue[username]
				sock.send("DONE".encode())
####################################################################
			elif Type == "ENDS":
				q = OnThrow(sock)
				Database.logQuestion(q)
				sock.send("DONE".encode())
####################################################################								
			elif Type == "CMPT":
				OnCommonPoint(sock)
				sock.send("DONE".encode())
####################################################################
			else:
				pass