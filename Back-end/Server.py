# Server.py
# - To-gather Server Program
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)
# Author @ Sungwoo Jeon (j0070ak@kaist.ac.kr)
import socket
from System import fork, lock, wait, alarm, repeat, cancel

class Server:
	LISTENQ = 1024

	def __init__(self, PORT):
		self.sock = socket.socket()
		self.sock.bind(('', PORT))
		self.sock.listen(Server.LISTENQ)
		self.clients = {}

		def accept_handler(argument):
			sock, clients, handler = argument
			while True:
				client, address = sock.accept()
				username = client.recv(64).strip().decode()
				clients[username] = client

				fork(handler, (client, username))

		fork(accept_handler, (self.sock, self.clients, self.per_clients))

	def per_clients(self, sock, username):
		while True:
			Type = sock.recv(4).decode()
			filename_length = sock.recv(4)
			filename_length = int.from_bytes(filename_length, 'big')
			filename = sock.recv(4).decode()
			data_length = sock.recv(8)
			data_length = int.from_bytes(data_length, 'big')
			data = sock.recv(datat_length).decode()

			if Type == "GET_":
				#To do get data from 'filename'
			elif Type == "POST":
				#to do post data into 'filename'