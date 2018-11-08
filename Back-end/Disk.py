# Disk.py
# - Disk Storage handler
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from pickle import dumps, loads, dump, load
from access_points import get_scanner

# class Database
# - database module
class Database:
	DB_PATH = "./Storage/"
	DB_PATH_HELP = DB_PATH + "Help"
	DB_PATH_LOCATION = DB_PATH + "Location/"
	DB_PATH_POKEMON = DB_PATH + "Pokemon/"

	@staticmethod
	def logHelp(user_from, user_to):
		try:
			with open(Database.DB_PATH_HELP, 'rb') as f:
				data = load(f)
		except:
			data = []

		data.append((user_from, user_to))
		with open(Database.DB_PATH_HELP, 'wb') as f:
			dump(data, f)

	@staticmethod
	def howManyHelp(user_from, user_to):
		try:
			with open(Database.DB_PATH_HELP, 'rb') as f:
				data = load(f)
		except:
			data = []

		n = 0
		for uf, ut in data:
			if uf == user_from and ut == user_to:
				n += 1
		return n

	@staticmethod
	def logQuestion(question):
		try:
			with open(Database.DB_PATH_QUESTION, 'rb') as f:
				data = load(f)
		except:
			data = []

		data.append(question)
		with open(Database.DB_PATH_QUESTION, 'wb') as f:
			dump(data, f)

	@staticmethod
	def getQuestions(question_id):
		try:
			with open(Database.DB_PATH_QUESTION, 'rb') as f:
				data = load(f)
		except:
			data = []

		return data

	@staticmethod
	def logLocation(username, location):
		with open(Database.DB_PATH_LOCATION + username, 'wb') as f:
			dump(location, f)

	@staticmethod
	def getLocation(username):
		try:
			with open(Database.DB_PATH_LOCATION + username, 'rb') as f:
				data = load(username)
		except:
			data = []

		return data

# class Question
# - contain question information
# - with answers related.
class Question:
	_ID_SERIAL = 0

	def __init__(self, questioner = None, text = None, question = None):
		self.questioner = questioner
		self.answers = []

		self.content_text = text
		self.comment_text = question

		if questioner != None and text != None and question != None:
			self.id = Question._ID_SERIAL
			Question._ID_SERIAL += 1
		else:
			self.id = -1

	def load(self, questioner, id, question, answers):
		self.questioner = questioner
		self.id = id
		self.question = question
		self.answers = answers

# class Answer
# - contain ansewr information
class Answer:
	_ID_SERIAL = 0

	def __init__(self, answerer = None, answer = None):
		self.answerer = answerer
		self.answer = answer

		if answerer != None and answer != None:
			self.id = Answer._ID_SERIAL
			Answer._ID_SERIAL += 1
		else:
			self.id = -1

	def load(self, answerer, id, answer):
		self.answerer = answerer
		self.id = id
		self.answer = answer