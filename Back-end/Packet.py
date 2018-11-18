# Packet.py
# - Packet
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from Disk import Format, Database, Rectangle
import socket

def GetHTTP(sock):
	header = []
	while True:
		d = sock.recv(1).decode()
		header.append(d)
		if ''.join(header[-4:]) == '\r\n\r\n':
			break

	header = ''.join(header)
	request = None
	command = None
	username = ''
	if header[:4] == 'POST':
		length = 0
		for line in header.split('\n'):
			if 'Content-Length' in line:
				length = int(line.split(':')[1].strip())
				break
		request = sock.recv(length).decode()

	for line in header.split('\n'):
		if 'From' in line:
			username = line.split(':')[1].strip()
		if 'CMD' in line:
			command = line.split(':')[1].strip()

	return username, command, request

def ResponseHTTP(sock, _response, additional = None):
	if additional != None:
		result = _response + '\n' + additional			# '\rDONE'
	else:
		result = _response

	response = '''HTTP/1.1 200 OK
Connection: close
Accept-Ranges: bytes
Content-Type: 

Access-Control-Allow-Origin: *
Access-Control-Allow-Method: *
Access-Control-Allow-Headers: *
Content-Length: %d

%s''' % (len(result), result)
	sock.send(response.encode())

def RecvFormat(body):
	lines = body.split('\n')

	# question information
	questioner = lines[0]
	question = lines[1]
	common = lines[2]

	# positions
	bRect_x1 = float(lines[3])
	bRect_y1 = float(lines[4])
	bRect_x2 = float(lines[5])
	bRect_y2 = float(lines[6])
	bRect_width = float(lines[7])
	bRect_height = float(lines[8])
	bRect = Rectangle(bRect_x1, bRect_y1, bRect_x2, bRect_y2, bRect_width, bRect_height)

	rect_size = int(lines[9])
	rects = []
	for i in range(rect_size):
		rect_x1 = float(lines[10 + 6*i])
		rect_y1 = float(lines[10 + 6*i + 1])
		rect_x2 = float(lines[10 + 6*i + 2])
		rect_y2 = float(lines[10 + 6*i + 3])
		rect_width = float(lines[10 + 6*i + 4])
		rect_height = float(lines[10 + 6*i + 5])
		rect = Rectangle(rect_x1, rect_y1, rect_x2, rect_y2, rect_width, rect_height)
		rects.append(rect)

	page = int(lines[-2])
	front_id = lines[-1]

	return Format(questioner, question, common, bRect, rects, page, front_id)

def _ofLength(s, n):
	return (str(s) + ' '*(n - len(str(s)))).encode()

def _ofBytes(d, n):
	return d.to_bytes(n, 'big')

def SendFormat(format):
	body = ''

	# question information
	body += format.questioner + '\n'
	body += format.comment_text + '\n'
	body += format.content_common + '\n'

	# position information
	if format.position_boundingRects != None:
		body += str(format.position_boundingRects.x1) + '\n'
		body += str(format.position_boundingRects.y1) + '\n'
		body += str(format.position_boundingRects.x2) + '\n'
		body += str(format.position_boundingRects.y2) + '\n'
		body += str(format.position_boundingRects.width) + '\n'
		body += str(format.position_boundingRects.height) + '\n'
	else:
		body += ("-1\n" * 6) 

	body += str(len(format.position_rects)) + '\n'
	for rect in format.position_rects:
		body += str(rect.x1) + '\n'
		body += str(rect.y1) + '\n'
		body += str(rect.x2) + '\n'
		body += str(rect.y2) + '\n'
		body += str(rect.width) + '\n'
		body += str(rect.height) + '\n'

	body += str(format.position_page) + '\n'
	body += format.front_id

	return body

def SendManyFormat(formats):
	body = ''
	for format in formats:
		sent = SendFormat(format)
		body += str(len(sent.split('\n'))) + '\n'
		body += sent + '\n'
	return body[:-1]

def SendEmptyFormat():
	return SendFormat(Format('', '', '', Rectangle(-1, -1, -1, -1, -1, -1), [], 0, ''))