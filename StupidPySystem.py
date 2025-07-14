import random, time, os, tkinter, requests

boot = False
quit = False
if boot == False:
    print("StupidPySystem Ver1\nPlease look at the first time guide before using")
    boot = True
while not quit:
    user = input("> ").lower().strip()
# This is the Help command.
    if user == "help":
        print("StupidPySystem Help\nReport any bugs you find!")
        user = input("help> ").lower().strip()
        if user == "exit":
            print("Exiting Help")
        elif user == "cmd":
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
        else:
            print("Command doesn't exist.")
# All of the Commands
    elif user == "cmd":
        print("opening cmd")
        os.system("cmd")
        quit = True
    elif user == "spsver":
        # I present, Code that most likely sucks because I followed a really bad guide!
        # Edit: It still sucks, I might change to customtkinter sometime in the near future
        spsversion = tkinter.Tk()

        spsversion.title("spsver")
        tkinter.Label(spsversion, text="StupidPySystem").pack()
        tkinter.Label(spsversion, text="Version 1 Beta\nWindows Build\nMade by @pepsicart. on Discord\npepsicarrt on Github").pack()
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
        quit = True
    elif user == "diskmgmt":
        print("close Disk Management to continue using SPS")
        os.system("diskmgmt.msc")
    elif user == "ping":
        # This command is due for a major rework sometime in the future
        # Currently it uses the standard Ping command in Windows
        print("This command is due for a major rework\nCurrently it uses the standard Ping command in Windows")
        user = input("What do you want to ping?\nping> ")
        os.system("ping "+user)
    elif user == "quit":
        quit = True
    else:
        print("That command doesn't exist yet, Check help for all of the commands.")