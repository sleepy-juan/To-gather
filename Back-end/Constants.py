# Constants.py
# - For Constants
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

class Protocol:
	class CLIENT:
		QUIT = "QUIT"					# GET
		POST_QUESTION = "POST"			# POST
		GET_QUESTIONS = "NTYQ"			# GET
		GET_QUESTION = "GETQ"			# GET
		ANSWER = "ANSW"
		GET_CONFIRMS = "NTYC"
		CONFIRM_ENDS = "ENDS"
		GET_ANSWERS = "GETA"
		LIST_MEMBERS = "LIST"
		GET_PUBLICS = "NTYP"
		GET_OWNS = "OWNS"

	class SERVER:
		OK = "DONE"
		NO_AVAILABLE_USER = "NO_AVAILABLE_USER"
		TIMED_OUT = "TIMED_OUT"
		DUPLICATED_QUESTION = "DUPLICATED_QUESTION"
		USERNAME_NOT_SET = "USERNAME_NOT_SET"
		WRONG_COMMAND = "WRONG_COMMAND"

	class INTS:
		TIME_OUT_IN_SECONDS = 5*60

class Status:
	class QUESTION:
		DELAYED = "DLYD"
		SENT = "SENT"
		ON_CONFIRM = "ONCF"

class Command:
	REMOVE_ANSWERS = "remove answers"
	REMOVE_QUESTIONS = "remove questions"