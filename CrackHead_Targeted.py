#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# from termcolor import colored
import sys
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

class airodump_Parameters_Targeted(object):

    def __init__(self, capture_Channel, capture_BSSID):
        self.capture_Channel = capture_Channel
        self.capture_BSSID = capture_BSSID

    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("Enter the CHANNEL of the device you want to TARGET: ")),
            str(raw_input("Enter the BSSID/Broadcast MAC Address of your TARGET: "))
                    )

user_input = airodump_Parameters_Targeted.from_input()
print 'Beginning targeted capture'
timestr = time.strftime("%Y%m%d-%H%M%S")

airodump_capture_filepath = "/root/WirelessAttackLite/logs/"
airodump_capture_file = airodump_capture_filepath + timestr + ".cap"
cmd_String = "airodump-ng --bssid {0} -c {1} --write {2} wlan1mon".format(
    user_input.capture_BSSID,
    user_input.capture_Channel,
    airodump_capture_file,
)
print cmd_String

os.system(cmd_String)
