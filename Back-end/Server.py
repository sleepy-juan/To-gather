# Server.py
# - To-gather Server Program
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)
# Author @ Sungwoo Jeon (j0070ak@kaist.ac.kr)
import socket
from Disk import get, post
from System import fork, lock, wait, alarm, repeat, cancel
from Packet import QuestionPacket

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
				clients[username] = client
				queue[username] = []

				fork(handler, (client, username, queue))

		fork(accept_handler, (self.sock, self.clients, self.per_clients, self.answer_queue))

	def per_clients(self, arg):
		sock, username, queue = arg
		while True:
			Type = sock.recv(4).decode()

			if Type == "THRW":
				q = OnThrow(sock)
				#Get list of users who did not received question.
				copy_ans = []
				for key in clients:
					copy_ans.append(key)
				for i in q.answer:
					copy_ans.remove(i.answerer)

				if len(copy_ans) == 0:
					#send packet to questioner
				else:
					user = copy_ans[random.randrange(0, len(coyp_ans))]
					A = q.answer[len(q.answer)-1]
					if (len(q.answer) == 0):
						answer_queue[user].append(q)
					elif (len(q.answer) >= 1):
						#Add answer into next user answer_queue
						answer_queue[user].append(q)
						#Remove answer from previous user answer_queue
						for i in answer_queue[q.answer[len(q.answer) - 1].answerer]:
							if (q.id == i.id):
								answer_queue[q.answer[len(q.answer) - 1].answerer].remove(i)
								break
				#send packet to user
			elif Type == "RECV":
				#to do something'
				pass