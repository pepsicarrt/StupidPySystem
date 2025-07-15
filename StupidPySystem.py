import random, time, os, requests
import tkinter as tk

os.system("cls")
spshelp = 0
print("StupidPySystem Ver1\nPlease look at the first time guide before using")
while True:
    user = input("> ").lower().strip()
    # This is the Help command.
    if user == "help":
        print("StupidPySystem Help\nReport any bugs you find!")
        while True:
            user = input("help> ").lower().strip()
            if user == "cmd":
                print("Command Prompt\n// Opens the Command Prompt (cmd)\n// Quits SPS")
            elif user == "powershell":
                print("Powershell\n// Opens Powershell\n// Quits SPS")
            elif user == "diskmgmt":
                print("Disk Management\n// Opens Disk Management\nAA")
            elif user == "spsver":
                print("SPS Ver\n// Just tells you the version of SPS")
            elif user == "winver":
                print("winver\n// Opens winver")
            elif user == "msinfo32":
                print("msinfo32\n// Opens msinfo32")
            elif user == "quit":
                print("Quit\n// Quits SPS")
            elif user == "ping":
                print("Ping\n// Uses the built in Ping command for whatever operating system you're using")
            elif user == "++":
                break
            else:
                print("Command doesn't exist.")
    # All of the Commands
    elif user == "cmd":
        print("opening cmd")
        os.system("cmd")
        break
    elif user == "spsver":
        # I present, Code that most likely sucks because I followed a really bad guide!
        # Edit: It still sucks, I might change to customtkinter sometime in the near future
        spsversion = tk.Tk()
        spsversion.title("spsver")
        tk.Label(spsversion, text="StupidPySystem").pack()
        tk.Label(spsversion, text="Version 1 Beta\nWindows Build\nMade by @pepsicart. on Discord\npepsicarrt on Github").pack()
        spsversion.minsize(220, 100)
        spsversion.maxsize(220, 100)
        spsversion.mainloop()
    elif user == "winver":
        os.system("winver")
    elif user == "msinfo32":
        os.system("msinfo32")
    elif user == "powershell":
        print("opening powershell\nmight take some time")
        os.system("powershell")
        break
    elif user == "diskmgmt":
        print("close Disk Management to continue using SPS")
        os.system("diskmgmt.msc")
    elif user == "ping":
        user = input("What do you want to ping?\nping> ").strip()
        if user == "":
            print("stop sleeping asshole")
            continue
        os.system("ping "+user)
    elif user == "quit":
        break
    else:
        print("That command doesn't exist yet, Check help for all of the commands.")