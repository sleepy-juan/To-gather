import socket
from Packet import OnRelayForOne
from Disk import Question, Answer
from access_points import get_scanner

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
sock.send(location.encode())

q1 = Question("juanlee", "What is your name?")
q1.answers.append(Answer("sungwoo", "I am sungwoo"))
q1.answers.append(Answer("sihyun", "I am sihyun"))

q2 = Question("juanlee", "What is Pen?")
q2.answers.append(Answer("sungwoo", "Apple Pen"))
q2.answers.append(Answer("sihyun", "Pineapple Pen"))

sock.send("THRW".encode())
OnRelayForOne(sock, q1)
print(sock.recv(4))

sock.send("THRW".encode())
OnRelayForOne(sock, q2)
print(sock.recv(4))

sock.send("QUIT".encode())

sock.close()