#!/usr/bin/env python
import requests
import subprocess, smtplib, re


def download(url):
    get_request = requests.get(url)
    # last element of list
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_request.content)



download("https://sites.google.com/site/eykmime/setupRenee64.zip")

# C:\Python27\python.exe -m pip install requests

