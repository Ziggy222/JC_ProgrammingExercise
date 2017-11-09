#Exercise 1: The goal of this exercise is to create a script that will enable and disable the "Guest" account
 #on a Mac/OSX Machine
# by Andrew Eagle
# November 8, 2017
#IMPORTS:
import os, os.path
import ctypes
import subprocess

#Ask the user whether to activate or deactivate the machines guest accounts
choice = input("Press 1 to Activate Guest Accounts. Press 2 to Deactivate Guest Accounts. Press Enter after either selection.\n")
choice = int(choice)
#if they choose to activate the accounts, attempt the command required.
if (choice == 1):
    status1 = subprocess.call(["sudo", "defaults", "write", "/Library/Preferences/com.apple.loginwindow", "GuestEnabled", "-bool", "YES"])
    #This will ask for password if sudo is not current
elif (choice == 2):
    status2 = subprocess.call(["sudo", "defaults", "write", "/Library/Preferences/com.apple.loginwindow", "GuestEnabled", "-bool", "NO"])
    #This will ask for password if sudo is not current
else:
    print ("Incorrect choice. Please try again with a proper input.")
