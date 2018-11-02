# Disk.py
# - Disk Storage handler
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from pickle import dumps, loads

class Question:
	def __init__(self, questioner = None, question = None):
		self.questioner = questioner
		self.question = question
		self.answers = []

	def dump(self):
		arg = [self.questioner, self.question, self.answers]
		return dumps(arg)

	def load(self, data):
		arg = loads(data)

		self.questioner = arg[0]
		self.question = arg[1]
		self.answers = arg[2]

class Answer:
	def __init__(self, answerer = None, answer = None):
		self.answerer = answerer
		self.answer = answer

	def dump(self):
		arg = [self.answerer, self.answer]
		return dumps(arg)

	def load(self, data):
		arg = loads(data)

		self.answerer = arg[0]
		self.answer = arg[1]