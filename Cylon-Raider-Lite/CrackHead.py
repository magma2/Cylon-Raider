#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# #from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen


# variable = __import__('module').class.variable


# os.system('cat /root/Cylon-Raider-Lite/banner_CrackHead.txt')
def airmon(): #No need for classes here, just one variable
    capture_Interface = str(raw_input("Enter the wireless INTERFACE that you want to capture with: "))
    cmd_String = "airmon-ng start %s" % capture_Interface
    print cmd_String
    os.system(cmd_String)
    #sample Join syntax (joins on the LEFT)
    # print ()"\n\t".join(capture_Interface))
    mon_String = "mon"
    airodump_String = capture_Interface + mon_String
    print 'Your airodump interface is...'
    print "Remember this string for the next step, AIRODUMP"
    main()
    return



def airodump():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. INFORMATION GATHERING, start Airodump to look for a good target to attack',
        '#2. TARGETED CAPTURE, change Airodump-ng parameters to capture packets of a targeted router'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Recon.py; exec bash\"'")
        airodump()
    elif opt_Choice == "0":
        main()
    elif opt_Choice == "2":
        os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Targeted.py; exec bash\"'")
        airodump()


        return
    else:
        print 'You have entered a invalid option'
        airodump()
    return


def aireplay():
    os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Replay.py; exec bash\"'")
    main()
    return

def aircrack():
    os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Aircrack.py; exec bash\"'")
    main()
    return

def main():
    opt_List = [
        '\n\t#1. AIRMON, start up the capture interface',
        '#2. AIRODUMP, begin scanning local access points in range and/or capture packets',
        '#3. AIREPLAY, send deauthorization packets to disconnect target clients and capture the 4-way handshake',
        '#4. AIRCRACK, attempt to crack the 4-way handshake with a wordlist (dictionary attack)'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        airmon()
    elif opt_Choice == "2":
        os.system('clear')
        airodump()
    elif opt_Choice == "3":
        os.system('clear')
        aireplay()
    elif opt_Choice == "4":
        os.system('clear')
        aircrack()
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
