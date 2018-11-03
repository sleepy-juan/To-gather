# System.py
# - simplified system functions
#
# Author @ Juan Lee (juanlee@kaist.ac.kr)

from threading import Thread
from threading import Lock

import time

# storage for storing static variables
class __Stored:
	_threads = []
	_threads_out_of_management = []
	_timers = []
	_timersRunning = []
	_lock = None

def _fork_out_of_management(fcnt, shared = None, daemon = True):
	thread = Thread(target = fcnt, args = (shared, ))
	thread.daemon = daemon
	__Stored._threads_out_of_management.append(thread)
	thread.start()

	return len(__Stored._threads_out_of_management) - 1

#################### THREAD FUNCTIONS ####################

# function fork: fcnt, [shared], [daemon] -> process_id
# - make process and run
def fork(fcnt, shared = None, daemon = True):
	thread = Thread(target = fcnt, args = (shared, ))
	thread.daemon = daemon
	__Stored._threads.append(thread)
	thread.start()

	return len(__Stored._threads) - 1

# function wait: [process_id] -> void
# - wait until given process is finishing
# - if pid is not given, it works for all threads
def wait(pid = None):
	if pid != None:
		if pid >= 0 and pid < len(__Stored._threads):
			__Stored._threads[pid].join()

		# store only alive threads
		alive_threads = []
		for thread in __Stored._threads:
			if thread.is_alive():
				alive_threads.append(thread)
		__Stored._threads = alive_threads
	else:
		while True:
			alive_threads = []
			for thread in __Stored._threads:
				if thread.is_alive():
					alive_threads.append(thread)
			if len(alive_threads) == 0:
				break;
		__Stored._threads = []

# function lock: void -> lock
# - return lock of python
def lock():
	if __Stored._lock == None:
		__Stored._lock = Lock()
	return __Stored._lock

#################### TIME MANAGEMENT FUNCTIONS ####################

# function alarm: fcnt, after, shared, daemon
# - after in seconds
def alarm(fcnt, after, shared = None, daemon = True):
	if after < 0:
		return

	def _helper(f, s, t, p):
		time.sleep(t)
		if __Stored._timersRunning[p]:
			f(s)
			__Stored._timersRunning[p] = False

	thread = Thread(target = _helper, args = (fcnt, shared, after, len(__Stored._timers)))
	thread.daemon = daemon
	__Stored._timers.append(thread)
	__Stored._timersRunning.append(True)
	thread.start()

	return len(__Stored._timers) - 1

# function repeat: fcnt, after, shared, daemon, first
# - after in seconds
def repeat(fcnt, after, shared = None, daemon = True, first = True):
	if after < 0:
		return

	def _helper(f, s, t, p, first):
		if first:
			f(s)
		time.sleep(t)
		if __Stored._timersRunning[p]:
			_helper(f, s, t, p, True)

	thread = Thread(target = _helper, args = (fcnt, shared, after, len(__Stored._timers), first))
	thread.daemon = daemon
	__Stored._timers.append(thread)
	__Stored._timersRunning.append(True)
	thread.start()

	return len(__Stored._timers) - 1

# function cancel: tid -> void
# - cancel the timer
def cancel(pid):
	__Stored._timersRunning[pid] = False