import socket

s = socket.socket()
s.bind(('', 12345))
s.listen(10)
c, n = s.accept()

b = []
while True:
	d = c.recv(1).decode()
	b.append(d)
	if ''.join(b[-4:]) == '\r\n\r\n':
		break

request = ''.join(b)
if request[:4] == 'POST':
	length = 0
	for line in request.split('\n'):
		if 'Content-Length' in line:
			length = line.split(':')[1].strip()
			length = int(length)
			break

	request += c.recv(length).decode()

print(request)

response = '''HTTP/1.1 200 OK
Connection: close
Accept-Ranges: bytes
Content-Type: text/html
Content-Length: 6

<html>'''

c.send(response.encode())

input()

c.close()
s.close()