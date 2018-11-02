# Disk.py
# - Disk Storage handler
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from pickle import dumps, loads

def _format(filename):
	return "./STORAGE/" + filename

def get(filename):
	try:
		with open(_format(filename), 'rb') as f:
			data = f.read()
		return data
	except:
		return None

def post(filename, payload):
	try:
		with open(_format(filename), 'wb') as f:
			f.wrtie(payload)
		return data
	except:
		return None