import socket
from Packet import OnRelay
from Disk import Question, Answer
from access_point import get_scanner

PORT = 12345

scanner = get_scanner()
aps = scanner.get_access_points()
location = list(map(lambda x:x.bssid, aps))
location = '\n'.join(location)

sock = socket.socket()
sock.connect(('127.0.0.1', PORT))

user = 'juanlee' + ' '*57
sock.send(user.encode())
sock.send(len(location).to_bytes(8, 'big'))
sock.send(location)

q = Question("juanlee", "What is your name?")
q.answers.append(Answer("sungwoo", "I am sungwoo"))
q.answers.append(Answer("sihyun", "I am sihyun"))

q = Question("juanlee", "What is Pen?")
q.answers.append(Answer("sungwoo", "Apple Pen"))
q.answers.append(Answer("sihyun", "Pineapple Pen"))

sock.send("THRW".encode())
OnRelay(sock, q)

sock.send("QUIT".encode())