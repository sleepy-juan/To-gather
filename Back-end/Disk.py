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
	DB_PATH_USER = DB_PATH + "User"

	@staticmethod
	def logHelp(user_from, user_to):
		try:
			with open(DB_PATH_HELP, 'rb') as f:
				data = load(f)
		except:
			data = []

		data.append((user_from, user_to))
		with open(DB_PATH_HELP, 'wb') as f:
			dump(data, f)

	@staticmethod
	def howManyHelp(user_from, user_to):
		try:
			with open(DB_PATH_HELP, 'rb') as f:
				data = load(f)
		except:
			data = []

		n = 0
		for uf, ut in data:
			if uf == user_from and ut == user_to:
				n += 1
		return n

	@staticmethod
	def logUser(user):
		try:
			with open(DB_PATH_USER, 'rb') as f:
				data = load(f)
		except:
			data = []

		data.append(user)
		with open(DB_PATH_USER, 'wb') as f:
			dump(data, f)

	@staticmethod
	def getUser(username):
		try:
			with open(DB_PATH_USER, 'rb') as f:
				data = load(f)
		except:
			data = []

		query = list(filter(lambda user: user.username == username))
		if len(query) == 0:
			return None
		return query[0]

	@staticmethod
	def logQuestion(question):
		try:
			with open(DB_PATH_QUESTION, 'rb') as f:
				data = load(f)
		except:
			data = []

		data.append(question)
		with open(DB_PATH_QUESTION, 'wb') as f:
			dump(data, f)

	@staticmethod
	def getQuestions(question_id):
		try:
			with open(DB_PATH_QUESTION, 'rb') as f:
				data = load(f)
		except:
			data = []

		return data

# class User
# - contain user information
class User:
	_ID_SERIAL = 0

	def __init__(self, username = None):
		if username != None:
			self.username = username

			scanner = get_scanner()
			aps = scanner.get_access_points()
			self.bssid = list(map(lambda x:x.bssid, aps))
			self.id = User._ID_SERIAL
			User._ID_SERIAL += 1
		else:
			self.username = None
			self.bssid = []
			self.id = -1

	def load(self, data):
		arg = loads(data)

		self.username = arg[0]
		self.bssid = arg[1]
		self.id = arg[2]

# class Question
# - contain question information
# - with answers related.
class Question:
	_ID_SERIAL = 0

	def __init__(self, questioner = None, question = None):
		self.questioner = questioner
		self.question = question
		self.answers = []

		if questioner != None and question != None:
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