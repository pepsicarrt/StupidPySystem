import random
import time
import os

somethingrandom = ["Pycharm", "Zen", "Firefox", "Rufus", "qBittorrent", "Steam", "Parsec", "1.1.1.1 (Warp)",
                   "VLC Media Player", "Retrobar", ]

quit = False
while not quit:
    user = input("> ").lower().strip()
# This is the Help command.
    if user == "help":
        print("could you like specify what you need help with")
        user = input("help> ").lower().strip()
        if user == "program":
            print(
                "Program\nVersion 1\n// Tells you a random program from a small list\n// Run using the command 'Program'")
        elif user == "cmd":
            print("Command Prompt\n// Opens the Command Prompt (cmd)\n// Quits SPS")
        elif user == "powershell":
            print("Powershell\n// Opens Powershell\n// Quits SPS")
        elif user == "diskmgmt":
            print("Disk Management\n// Opens Disk Management\nAA")
        elif user == "spsver":
            print("SPS Ver\n// Just tells you the version of SPS")
        elif user == ("winver"):
            print("winver\n// Opens winver")
        elif user == ("msinfo32"):
            print("msinfo32\n// Opens msinfo32")
        elif user == "quit":
            print("Quit\n// Quits SPS")
        else:
            print("Command doesn't exist.")
# All of the Commands
    elif user == "program":
        print(random.choice(somethingrandom))
    elif user == "cmd":
        print("opening cmd")
        os.system("cmd")
        quit = True
    elif user == "spsver":
        print("StupidPySystem\n// Version 1B\n// Windows Build\n// made by @pepsicart on Discord\n// pepsicarrt on GitHub")
    elif user == "winver":
        os.system("winver")
    elif user == "msinfo32":
        os.system("msinfo32")
    elif user == "powershell":
        print("opening powershell\nmight take some time")
        os.system("powershell")
        quit = True
    elif user == "diskmgmt":
        print("close Disk Management to continue using SPS")
        os.system("diskmgmt.msc")
    elif user == "quit":
        quit = True