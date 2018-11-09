# Constants.py
# - For Constants
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

class Protocol:
	class CLIENT:
		QUIT = "QUIT"
		POST_QUESTION = "POST"
		GET_QUESTIONS = "NTYQ"
		GET_QUESTION = "GETQ"
		ANSWER = "ANSW"
		GET_CONFIRMS = "NTYC"
		CONFIRM_ENDS = "ENDS"
		GET_ANSWERS = "GETA"

	class SERVER:
		OK = "DONE"
		NO_AVAILABLE_USER = "NUSR"
		TIMED_OUT = "TMDT"
		DUPLICATED_QUESTION = "DUPQ"

	class INTS:
		TIME_OUT_IN_SECONDS = 30

class Status:
	class QUESTION:
		DELAYED = "DLYD"
		SENT = "SENT"
		ON_CONFIRM = "ONCF"