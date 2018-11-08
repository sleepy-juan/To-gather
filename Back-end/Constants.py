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

	class SERVER:
		OK = "DONE"
		NO_AVAILABLE_USER = "NUSR"
		TIMED_OUT = "TMDT"
		WRONG_COMFIRMATION = "WRNC"

	class INTS:
		TIME_OUT_IN_SECONDS = 5 * 60