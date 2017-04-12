# Cylon Raider (Formerly Known as Wireless-Attack-Lite)
Easy and quick automation of Aircrack-ng "Replay-Attacks", targeting WPA2-PSK encrypted routers (most home NATed networks and many small businesses). Guaranteed to capture the 4-way handshake of a decently populated router in under 10 minutes (at least 1 or 2 people logged onto router to properly de-authenticate and listen for their creds). 

It can also detect and decloak hidden networks (see UNCLOAK HIDDEN NETWORKS) below



Lightweight Version of Wifi-Attack-Autoloader for Outdated Releases of Kali Nethunter Devices(Python 2.7.9)
Designed to Capture the Handshake in Record Time so you can GTFO out of that area!
Does not support WPS-Enabled Attacks (also known as "Reaver"), see bottom "Why No WPS?"

# Who is this for?
1. Anyone stuck with a crappy Asus Nexus 7 Tablet (2012), or any other device no longer officially supported by the Kali Nethunter Project. It sure kept my crappy tablet useful!
2. Anyone dissatisfied with modern GUI versions of Wi-Fi Cracking software (Wifite was supposed to be something awesome, but disappointingly it took damn near forever and did not send enough deauth packets), I can capture the 4-Way WPA2-PSK Handshake in seconds using this, a automated version of Airmon/Aircrack. All it requires is a decent amount of clients on a wireless network for it to work. 
3. Sometimes referring back to the command line is a way better idea than rely on some GUI crap. It helps you maintain a better understanding of what is going on (or going wrong). 

# Installation
1. Unzip the contents of the repo (or even better, git clone it)

"cd /tmp"

"git clone https://github.com/tanc7/Cylon-Raider"

2. Run autoInstallerNethunter.sh

"cd /tmp/Cylon-Raider/"

"chmod 777 autoInstallerNethunter.sh"

"./autoInstallerNethunter.sh"

This automatically makes the directory, sets the proper permissions, and also drops the primary scripts into your nethunter device's /root directory (see scripts)

# Script Features and Recommended Order of Operations
Steps 1 to 5 covered here in this video: https://raw.githubusercontent.com/tanc7/Cylon-Raider/master/How-To-Videos/How-To-Video-Wireless-Attack-Lite.webm

STEP ONE: Insert External wireless card + OTG cable into Nethunter tablet/phone, and run /root/monitorMode.sh

STEP TWO: Run /root/scanMode.sh, wait patiently for all wireless APs to show up, press Ctrl+C to freeze it and copy/paste the BSSID/MAC of the device you want to capture the handshake of

STEP THREE: Run /root/targetedMode.sh, enter the Channel and BSSID of the device you are targeted

STEP FOUR: Open another nethunter terminal and run /root/replayAttack.sh, usually between 100 to 2000 packets is recommended

STEP FIVE: It's done when you see on the top right corner of the terminal "WPA Handshake: BSSID". You can GTFO out of there now

GO HOME: And start cracking that password with /root/crack_WPA_handshake.sh, you do not need to be around the attacked AP anymore. Not until you crack that password!

Cracking handshake covered here: https://raw.githubusercontent.com/tanc7/Cylon-Raider/master/How-To-Videos/How-To-Crack-Handshake.webm

# Other Scripts Below

# UNCLOAK HIDDEN NETWORKS: 

Adopted from Violent Python, /root/hiddenNetworkSniffer.sh, give it some time. First it'll detect the BSSID, and then a few minutes later it'll reveal the SSID. The name of the SSID isn't the important part though, and the owner may as well have changed it. To me, it's the BSSID/MAC that counts

# CREDIT CARD SNIFFER:

Should be used either with Monitor Mode On, OR, even better, after you cracked the password and logged back into their network. 

# Why is WPS PIN Cracking not Recommended? (Changed from "Why No WPS")

I am not exactly sure why this README update reverted. It was supposed to be like this since the Heavy-Raider module launched. But from all the TLDR bs below, the question I want to ask you, the user, is... "Do you want to spend 10 hours creeping outside someone's house, cracking a WPS pin because there is no actual handshake (for WPS)?". By applying the "guerilla warfare tactic" using the "Standard Cylon Raider procedure", I can capture the handshake (of a decently populated router) in less than ten minutes (10 being pretty excessive actually), go back home, start up Aircrack-ng and make me a sandwich.

Another question, "Do you want to have your victim freak out and send the dogs after you? Or a cop to crack a T-baton over your head?" 


Attacking WPS-Enabled Services means that the admin or owner of the router enabled WPS. You cannot use Reaver against some router that doesnt have WPS Enabled. 

Secondly, the disadvantages of WPS is becoming more of a mainstream knowledge. Less and less wireless APs are employing WPS. 
http://tools.kali.org/wireless-attacks/reaver
