# Packet.py
# - Packet
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from Disk import Format, Database, Rectangle
import socket

def RecvUsername(sock):
	username = sock.recv(64).strip().decode()
	return username

def RecvFormat(sock):
	# question information
	questioner = sock.recv(64).strip().decode()
	question_length = int.from_bytes(sock.recv(8), 'big')
	question = sock.recv(question_length).strip().decode()
	text_length = int.from_bytes(sock.recv(8), 'big')
	text = sock.recv(text_length).strip().decode()
	common = sock.recv(64).strip().decode()

	# positions
	bRect_x1 = float(sock.recv(64).strip().decode())
	bRect_y1 = float(sock.recv(64).strip().decode())
	bRect_x2 = float(sock.recv(64).strip().decode())
	bRect_y2 = float(sock.recv(64).strip().decode())
	bRect_width = float(sock.recv(64).strip().decode())
	bRect_height = float(sock.recv(64).strip().decode())
	bRect = Rectangle(bRect_x1, bRect_y1, bRect_x2, bRect_y2, bRect_width, bRect_height)

	rect_size = int.from_bytes(sock.recv(4), 'big')
	rects = []
	for i in range(rect_size):
		rect_x1 = float(sock.recv(64).strip().decode())
		rect_y1 = float(sock.recv(64).strip().decode())
		rect_x2 = float(sock.recv(64).strip().decode())
		rect_y2 = float(sock.recv(64).strip().decode())
		rect_width = float(sock.recv(64).strip().decode())
		rect_height = float(sock.recv(64).strip().decode())
		rect = Rectangle(rect_x1, rect_y1, rect_x2, rect_y2, rect_width, rect_height)
		rects.append(rect)

	page = int.from_bytes(sock.recv(4), 'big')
	front_id = sock.recv(64).strip().decode()

	return Format(questioner, text, common, question, bRect, rects, page, front_id)

def _ofLength(s, n):
	return (str(s) + ' '*(n - len(s))).encode()

def _ofBytes(d, n):
	return d.to_bytes(n, 'big')

def SendFormat(sock, format):
	# question information
	sock.send(_ofLength(format.questioner, 64))
	sock.send(_ofBytes(len(format.comment_text, 8)))
	sock.send(format.comment_text.encode())
	sock.send(_ofBytes(len(format.content_text, 8)))
	sock.send(format.content_text.encode())
	sock.send(_ofLength(format.content_common, 64))

	# position information
	sock.send(_ofLength(format.position_boundingRects.x1, 64))
	sock.send(_ofLength(format.position_boundingRects.y1, 64))
	sock.send(_ofLength(format.position_boundingRects.x2, 64))
	sock.send(_ofLength(format.position_boundingRects.y2, 64))
	sock.send(_ofLength(format.position_boundingRects.width, 64))
	sock.send(_ofLength(format.position_boundingRects.height, 64))

	sock.send(_ofBytes(len(format.rects), 4))
	for rect in format.position_rects:
		sock.send(_ofLength(rect.x1, 64))
		sock.send(_ofLength(rect.y1, 64))
		sock.send(_ofLength(rect.x2, 64))
		sock.send(_ofLength(rect.y2, 64))
		sock.send(_ofLength(rect.width, 64))
		sock.send(_ofLength(rect.height, 64))

	sock.send(_ofBytes(format.position_page, 4))
	sock.send(_ofLength(format.front_id, 64))

def SendEmptyFormat(sock):
	SendFormat(Format('', '', ''. '', Rectangle(-1, -1, -1, -1, -1, -1), [], '', ''))

def SendIds(sock, ids):
	sock.send(_ofBytes(len(ids), 4))
	for i in ids:
		sock.send(_ofLength(i, 64))