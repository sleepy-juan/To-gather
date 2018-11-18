import random

SCHOOL = ['KAIST', 'POSTECH']
GRADE = ['1','2','3','4']
MAJOR = ['CS', 'MAS', 'ME']
LOCATION = ['KOREA', 'FOREIGN']
CLUB = ['ART', 'MUSIC', 'EXERCISE']

def common():
	user_info = {}
	user_info['school'] = SCHOOL[random.randrange(0, len(SCHOOL))]
	user_info['grade'] = GRADE[random.randrange(0, len(GRADE))]
	user_info['major'] = MAJOR[random.randrange(0, len(MAJOR))]
	user_info['location'] = LOCATION[random.randrange(0, len(LOCATION))]
	user_info['club'] = CLUB[random.randrange(0, len(CLUB))]
	return user_info

def user_common(map, userA, userB):
	for i in map[userA]:
		if map[userA][i] == map[userB][i]:
			return i
	return 'none'

answerer = 
questioner = 
if Database.howManyHelp() == 0:
	question.content_common = user_common(user_info, answerer, questioner)
else:
	question.content_common = 'help' + str(Database.howManyHelp())