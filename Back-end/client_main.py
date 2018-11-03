import socket
from Packet import OnRelayForOne, OnThrow
from Disk import Question, Answer
from access_points import get_scanner
from System import fork, repeat

IP = '127.0.0.1'
PORT = 12345

scanner = get_scanner()
aps = scanner.get_access_points()
location = list(map(lambda x:x.bssid, aps))
location = '\n'.join(location)

usernames = [
	'Juan Lee',
	'Sungwoo Jeon',
	'Sihyun Yu',
	'Minji Lee',
	'Prime Kang',
	'Kihoon Kwon',
	'Jongho Lee',
	'Youngmoo Kim',
	'Yongwon Cho',
	'Daho Jung',
	'Hyunchang Oh',
	'Changhyun Park',
	'Jihoon Baek',
	'Ilju Ko',
	'Beomseok Oh',
]

use_socket = [False] * len(usernames)

def relay_handler(arg):
	sock, username = arg

	sock.send("RELY".encode())
	size = sock.recv(4)
	size = int.from_bytes(size, 'big')

	for i in range(size):
		q = OnThrow(sock)
		print(username, '@', q.question)

	sock.recv(4)

peers = []
for username in usernames:
	peer = socket.socket()
	peer.connect((IP, PORT))

	user = username + ' '*(64 - len(username))
	peer.send(user.encode())
	peer.send(len(location).to_bytes(8, 'big'))
	peer.send(location.encode())

	peers.append(peer)

	repeat(relay_handler, 1, (peer, username))

q1 = Question("juanlee", "What is your name?")
q1.answers.append(Answer("sungwoo", "I am sungwoo"))
q1.answers.append(Answer("sihyun", "I am sihyun"))

while True:
	q = input()
	if q == 'q': break

	peers[0].send("THRW".encode())
	OnRelayForOne(peers[0], q1)
	
	print(peers[0].recv(4))

for peer in peers:
	peer.send("QUIT".encode())
	peer.close()