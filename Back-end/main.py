from Server import Server
import sys

s = Server(int(sys.argv[1]))

while True:
	cmd = input()
	if cmd.lower() == 'q':
		break
	s.run_command(cmd.lower())

s.close()