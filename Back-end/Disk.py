# Disk.py
# - Disk Storage handler
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from pickle import dumps, loads, dump, load

# class Database
# - database module
class Database:
	DB_PATH = "./Storage/"
	DB_PATH_HELP = DB_PATH + "Help"
	DB_PATH_QUESTION = DB_PATH + "QUESTION/"
	DB_PATH_ANSWER = DB_PATH + "ANSWER/"

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
		path = Database.DB_PATH_QUESTION + str(question.front_id)
		with open(path, 'wb') as f:
			dump(question, f)

	@staticmethod
	def getQuestion(question_id):
		path = Database.DB_PATH_QUESTION + str(question_id)
		try:
			with open(path, 'rb') as f:
				data = load(f)
		except:
			data = None

		return data

	@staticmethod
	def logAnswer(answer):
		path = Database.DB_PATH_ANSWER + str(answer.front_id)
		try:
			with open(path, 'rb') as f:
				data = load(f)
		except:
			data = []

		data.append(answer)
		with open(path, 'wb') as f:
			dump(data, f)

	@staticmethod
	def getAnswer(answer_id):
		path = Database.DB_PATH_ANSWER + str(answer_id)
		try:
			with open(path, 'rb') as f:
				data = load(f)
		except:
			data = []

		return data

# class Rectangle
class Rectangle:
	def __init__(self, x1 = None, y1 = None, x2 = None, y2 = None, width = None, height = None):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.width = width
		self.height = height

	def toTuple(self):
		return (self.x1, self.y1, self.x2, self.y2, self.width, self.height)

	def fromTuple(self, t):
		self.x1 = t[0]
		self.y1 = t[1]
		self.x2 = t[2]
		self.y2 = t[3]
		self.width = t[4]
		self.height = t[5]

# class Format
# - contain question information
# - with answers related.
class Format:
	def __init__(self, questioner = None, text = None, question = None, common = None, bRect = None, rects = None, page = None, front_id = None):
		self.questioner = questioner

		self.content_text = text
		self.content_common = common
		self.comment_text = question

		self.position_boundingRects = bRect
		self.position_rects = rects
		self.position_page = page

		self.front_id = front_id

	def load(self, questioner, text, common, question, bRect, rects, page, front_id):
		self.questioner = questioner
		self.content_text = text
		self.content_common = common
		self.comment_text = question

		self.position_boundingRects = Rectangle()
		self.position_boundingRects.fromTuple(bRect)
		self.position_page = page

		self.front_id = front_id

		self.position_rects = []
		for rect in rects:
			r = Rectangle()
			r.fromTuple(rect)
			self.position_rects.append(r)