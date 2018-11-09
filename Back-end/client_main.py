import socket
import sys
from Packet import *
from Constants import Protocol

ip = '127.0.0.1'
username = sys.argv[1]

port = 12345
if len(sys.argv) == 3:
	port = int(sys.argv[2])

def _ofLength(s, n):
	return (str(s) + ' '*(n - len(str(s)))).encode()

def _ofBytes(d, n):
	return d.to_bytes(n, 'big')

sock = socket.socket()
sock.connect((ip, port))
sock.send(_ofLength(username, 64))

while True:
	cmd = input(">> ")
	if cmd not in [Protocol.CLIENT.QUIT, Protocol.CLIENT.POST_QUESTION, Protocol.CLIENT.GET_QUESTIONS, Protocol.CLIENT.GET_QUESTION, Protocol.CLIENT.ANSWER, Protocol.CLIENT.GET_CONFIRMS, Protocol.CLIENT.CONFIRM_ENDS, Protocol.CLIENT.GET_ANSWERS]:
		continue
	sock.send(cmd.encode())
####################################################################
	if cmd == Protocol.CLIENT.QUIT:
		sock.close()
		break
####################################################################
	elif cmd == Protocol.CLIENT.POST_QUESTION:
		text = "text"
		question = input("Question: ")
		bRect = Rectangle(0,0,0,0,0,0)
		page = 1
		front_id = input("ID: ")

		f = Format(username, text, question, '', bRect, [bRect], page, front_id)
		SendFormat(sock, f)
####################################################################
	elif cmd == Protocol.CLIENT.GET_QUESTIONS:
		ids = RecvIds(sock)
		print(ids)
####################################################################
	elif cmd == Protocol.CLIENT.GET_QUESTION:
		qid = input("ID: ")
		sock.send(_ofLength(qid, 64))
		f = RecvFormat(sock)

		print("-- question:", f.comment_text)
		print("-- questioner:", f.questioner)
		print("-- page:", f.position_page)
		print("-- common:", f.content_common)
####################################################################
	elif cmd == Protocol.CLIENT.ANSWER:
		question = input("Answer: ")
		front_id = input("ID: ")

		f = Format(username, '', question, '', None, [], 1, front_id)
		SendFormat(sock, f)
####################################################################
	elif cmd == Protocol.CLIENT.GET_CONFIRMS:
		ids = RecvIds(sock)
		print(ids)
####################################################################
	elif cmd == Protocol.CLIENT.CONFIRM_ENDS:
		front_id = input("ID: ")
		sock.send(_ofLength(front_id, 64))
####################################################################
	elif cmd == Protocol.CLIENT.GET_ANSWERS:
		front_id = input("ID: ")
		sock.send(_ofLength(front_id, 64))
		answers = RecvManyFormat(sock)
		for answer in answers:
			print("%s answers %s" % (answer.questioner, answer.comment_text))
	
	print(sock.recv(4).decode())