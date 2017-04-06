# Wireless-Attack-Lite
Lightweight Version of Wifi-Attack-Autoloader for Outdated Releases of Kali Nethunter (Python 2.7.9)
Designed to Capture the Handshake in Record Time so you can GTFO out of that area!
Does not support WPS-Enabled Attacks (also known as "Reaver"), see bottom "Why No WPS?"

# Who is this for?
1. Anyone stuck with a crappy Asus Nexus 7 Tablet (2012), or any other device no longer officially supported by the Kali Nethunter Project. It sure kept my crappy tablet useful!
2. Anyone dissatisfied with modern GUI versions of Wi-Fi Cracking software (Wifite was supposed to be something awesome, but disappointingly it took damn near forever and did not send enough deauth packets), I can capture the 4-Way WPA2-PSK Handshake in seconds using this, a automated version of Airmon/Aircrack. All it requires is a decent amount of clients on a wireless network for it to work. 
3. Sometimes referring back to the command line is a way better idea than rely on some GUI crap. It helps you maintain a better understanding of what is going on (or going wrong). 

# Installation
1. Unzip the contents of the repo (or even better, git clone it)
2. Run autoInstaller.sh
3. Navigate to /root/WirelessAttackLite
4. For NetHunter devices you want to use the /KaliTerminalScripts folder instead (see below)

# General Steps of Operation

Navigate to /root/WirelessAttackLite/KaliTerminalScripts

1. Run monitorMode.sh to put your external wireless card + OTG cable into monitor mode
2. Ctrl + C to freeze monitor mode when you find a target
3. Locate a BSSID of your target and then run targetedMode.sh
4. In targetedMode.sh enter the BSSID MAC of target to only capture packets of that device
5. Open a new terminal and run replayAttack.sh, enter BSSID MAC + # of deauth packets you want to send (recommended between 100 to 1000)
6. If you are successful with capturing the 4-way handshake, the terminal running targetedMode.sh will say WPA-Handshake on the top-right
7. You should LEAVE the area as soon as you capture the 4-way handshake. 
8. Cracking the handshake could be done at home 

Steps 1 to 7 only takes at most, 10 minutes

Step 8 could take days depending on the quality of your wordlist (Dictionary Attack)

# Why No WPS?
Attacking WPS-Enabled Services means that the admin or owner of the router enabled WPS. You cannot use Reaver against some router that doesnt have WPS Enabled. 

Secondly, the disadvantages of WPS is becoming more of a mainstream knowledge. Less and less wireless APs are employing WPS. 

If you have the fortune of finding a WPS-Enabled AP, then by all means, use Reaver because that is now the best option: http://tools.kali.org/wireless-attacks/reaver
