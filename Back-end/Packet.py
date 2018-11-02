# Packet.py
# - Packet
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from Disk import Question, Answer
import socket

def OnThrow(sock):
	questioner = sock.recv(64).strip().decode()
	question_id = sock.recv(4)
	question_id = int.from_bytes(question_id, 'big')
	question_length = sock.recv(8)
	question_length = int.from_bytes(question_length, 'big')
	question = sock.recv(question_length).strip().decode()

	n_answers = sock.recv(4)
	n_answers = int.from_bytes(n_answers, 'big')

	answers = []
	for i in range(n_answers):
		answerer = sock.recv(64).strip().decode()
		answer_id = sock.recv(4)
		answer_id = int.from_bytes(answer_id, 'big')
		answer_length = sock.recv(8)
		answer_length = int.from_bytes(answer_length, 'big')
		answer = sock.recv(answer_length).strip().decode()

		answer_object = Answer()
		answer_object.load(answerer, answer_id, answer)
		answers.append(answer_object)

	question_object = Question()
	question_object.load(questioner, question_id, question, answers)
	return question_object

def OnRelayForOne(sock, q):
	questioner = (q.questioner + ' '*(64 - len(q.questioner))).encode()
	sock.send(questioner)

	question_id = q.id.to_bytes(4, 'big')
	sock.send(question_id)

	question_length = len(q.question).to_bytes(8, 'big')
	sock.send(question_length)

	sock.send(q.question.encode())

	n_answers = len(q.answers).to_bytes(4, 'big')
	sock.send(n_answers)

	answers = []
	for a in q.answers:
		answerer = (a.answerer + ' '*(64 - len(a.answerer))).encode()
		sock.send(answerer)

		answer_id = a.id.to_bytes(4, 'big')
		sock.send(answer_id)

		answer_length = len(a.answer).to_bytes(8, 'big')
		sock.send(answer_length)

		sock.send(a.answer.encode())

def OnRelay(sock, qs):
	question_number = len(qs).to_bytes(4, 'big')
	sock.send(question_number)

	for q in qs:
		OnRelayForOne(sock, q)