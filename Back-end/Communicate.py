# Communicate.py
# - Communication Module for both client and server
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

import socket
import pickle
from access_points import get_scanner

######################################################################
# Communicate                                                        #
#                                                                    #
# Server Side:                                                       #
#   - askConfirm(user, answer)                                       #
#   - throwQuestion(user_pool, question).                            #
#   - assignPokemon(user)                                            #
#                                                                    #
# Client Side:                                                       #
#   - ask(question)                                                  #
#   - answer(question)                                               #
#   - confirm(answer, decision)                                      #
#   - askPokemon()                                                   #
######################################################################

########################     Parameters     ##########################

# class User
# - define user information
class User:
	# constructor: username, email
	def __init__(self, username, email):
		self.username = username
		self.email = email

	def where(self):
		# get current position
		scanner = get_scanner()
		access_points = scanner.get_access_points()
		self.positions = list(map(lambda x:x.bssid, access_points))

	def get(self):
		return pickle.dumps([self.username, self.email, self.positions])

	def set(self, info):
		parsed = pickle.loads(info)

		self.username = parsed[0]
		self.email = parsed[1]
		self.positions = parsed[2]

# class Question
# - define Question information
class Question:
	# constructor: 
	def __init__(self, )

########################     Server Side     #########################

# class ServerSide
class ServerSide:
	# constructor: void
	def __init__(self):
		pass

	# askConfirm: user, answer