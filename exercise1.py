#Exercise 1: The goal of this exercise is to create a script that will enable and disable the "Guest" account on a Windows Machine
# by Andrew Eagle
# November 7, 2017
#IMPORTS:
import os, os.path
import ctypes
import subprocess


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():

    #Ask the user whether to activate or deactivate the machines guest accounts
    choice = input("Press 1 to Activate Guest Accounts. Press 2 to Deactivate Guest Accounts. Press Enter after either selection.\n")
    choice = int(choice)
    if (choice == 1):
        status1 = subprocess.call("start /wait cmd /c net user guest /active:yes", shell=True)
    elif (choice == 2):
        status2 = subprocess.call("start /wait cmd /c net user guest /active:no", shell=True)
    else:
        print ("Incorrect choice. Please try again with a proper input.")
else:
    #If not admin, inform of failure.
    print ("Process failed. This script requires Admin rights, retry as admin.")
