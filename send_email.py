#!/usr/bin/env python

import subprocess, smtplib


def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)       
    server.starttls()
    # login to email
    server.login(email, password)
    server.sendmail(email, email, message)     # from to content
    server.quit()

send_email("testaccount@gmail.com", "testpassword", "result")

