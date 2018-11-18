import random

DORM = ['Heemang', 'Areum']
GRADE = ['1','2','3','4']
MAJOR = ['CS', 'MAS', 'ME']
LOCATION = ['KOREA', 'FOREIGN']
CLUB = ['ART', 'MUSIC', 'EXERCISE']

def common():
	user_info = {}
	user_info['we are in same dormitory'] = DORM[random.randrange(0, len(DORM))]
	user_info['we are in same grade'] = GRADE[random.randrange(0, len(GRADE))]
	user_info['we have same major'] = MAJOR[random.randrange(0, len(MAJOR))]
	user_info['we are in same location'] = LOCATION[random.randrange(0, len(LOCATION))]
	user_info['we have same club'] = CLUB[random.randrange(0, len(CLUB))]
	return user_info

def user_common(map, userA, userB):
	for i in map[userA]:
		if map[userA][i] == map[userB][i]:
			return i
	return 'none'
