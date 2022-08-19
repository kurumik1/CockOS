#imports
import os
import time #i invented time
import linecache
import random
import socket
import subprocess
import sys
import CockAssEmbly #fune
import cv2
import string
from pywebcopy import save_webpage
from playsound import playsound
#import aydans brain
#ModuleNotFoundError: No module named 'aydans brain'

pyloc = os.getcwd()
filesystemlocation = pyloc + os.path.normpath("/")
curdir = "FileSys\\"

def getcommand(inpute):
    all_words = inpute.split()
    try:
        first_word= all_words[0]
        second_word= all_words[1]
        return first_word, second_word
    except:
        try:
            return first_word, "error"
        except:
            return "error", "error"
with open(pyloc + "\sysf\SYSSTATS.cfg") as f:
    Lines = f.readlines()
    linenum = 0
    for line in Lines:
        linenum = linenum + 1
        if linenum == 1:
            osn = line
        if linenum == 2:
            ver = line
        if linenum == 3:
            tsu = line
    newtsu = int(tsu) + 1
with open(pyloc + "\SYSSTATS.cfg", "w") as f:
    f.write(osn + ver + str(newtsu))

print(r"""\

 __      __   _                    _____       ___         _    ___  ___ 
 \ \    / /__| |__ ___ _ __  ___  |_   _|__   / __|___  __| |__/ _ \/ __|
  \ \/\/ / -_) / _/ _ \ '  \/ -_)   | |/ _ \ | (__/ _ \/ _| / / (_) \__ \
   \_/\_/\___|_\__\___/_|_|_\___|   |_|\___/  \___\___/\__|_\_\\___/|___/
                                                                         
            """)
playsound(pyloc + "\sysf" + "\startupshort.wav")
while True:
    val = input(curdir + " -> ")
    command, value = getcommand(val)
    if command.lower() == "setdir":
        if not value == "error":
            if value.lower() == "documents":
                dir = "FileSys\Documents"
            elif value.lower() == "programs":
                dir = "FileSys\Programs"
            else:
                dir = value
            ACTUALdir = pyloc + "\\" + dir
            #print(ACTUALdir)
            if not os.path.exists(ACTUALdir): #hahah fune numba
                dir = curdir
                print("Invalid Directory!")
                playsound(pyloc + "\sysf" + "\\" + "blip.wav")
            else:
                curdir = dir
        else:
            print("Enter a directory after setdir")
            playsound(pyloc + "\sysf" + "\\" + "blip.wav")
    if command.lower() == "open":
        if not value == "error":
            print(dir)
            File = pyloc + "\\" + dir + "\\" + value
            filename, fext = os.path.splitext(File)
            if fext == ".cok":
                CockAssEmbly.readCockScript(File)
            if fext == ".txt":
                with open(File) as f:
                    lines = f.readlines()
                print(lines)
            if fext == ".png":
                print(File)
                img = cv2.imread(File, cv2.IMREAD_ANYCOLOR)
                cv2.imshow("Image", img)
                cv2.waitKey(0)
        else:
            print("Enter a file name")
            playsound(pyloc + "\sysf" + "\\" + "blip.wav")
    if command.lower() == "write":
        if not value == "error":
            File = pyloc + r"\\" + dir + "\\" + value
            filename, fext = os.path.splitext(File)
            if fext == ".txt":
                with open(File, 'w') as f:
                    f.write(input("What to write? "))
                print(lines)
        else:
            print("Enter a file name")
            playsound(pyloc + "\sysf" + "\\" + "blip.wav")
    if command.lower() == "dircont":
        with os.scandir(pyloc + r"\\" + dir) as entries:
            print("Contents in directory " + dir)
            for entry in entries:
                print(entry.name)
    if command.lower() == "getip":
        print(socket.gethostbyname(socket.gethostname()))
    if command.lower() == "downloadwebsite":
        kwargs = {'bypass_robots': True, 'project_name': 'websitedownload'}
        save_webpage(value, pyloc + '\FileSys\DLWS', **kwargs)
    if command.lower() == "win10cmd":
        fuckand = input("CMD input: ")
        rv = os.system(fuckand)
        print(rv)
    if command.lower() == "repeat":
        if value:
            print(value)
        else:
            print("Enter something to repeat")
    if command.lower() == "exit":
        sys.exit("Ran command exit")
    if command.lower() == "sex":
        print("*sex noises*") #haha get it its sex so its fune
    if command.lower() == "randomword":
        wordlist = ["Car","Truck","Idiot","That","Is","Dumb","ur mother","Balls","Then","There","Plane","Tower","Explosion","Causes","Shoots","Racism","CEO","Of","Why","Does","Yellow","Red","Blue","White","Black","Course","Cock and ball torture","Twitter","Shit","Man","User","Math","School","Sucks","Cock","Hey","Guys","The","Bald","Twitter","Shit","Man","AI","Horse","Dog","Walks","Into","House","Massive","World","Medic","Ass","Supreme","Train","Pisses","Hot","Sex","Long","Sandwich","Word","A","An","Roblox","What is a","Fun Fact:","Apple","Microsoft","Converstration","Says","Breaking News:","Unarmed","Armed","Assault","Toilet","Breaker"]
        howmanywords = input("How many words: ")
        Sentence = ""
        for x in range(int(howmanywords)):
            Sentence = Sentence + random.choice(wordlist) + " "
        print(Sentence)
    if command.lower() == "systemstats":
        with open(pyloc + "\SYSSTATS.cfg") as f:
            Lines = f.readlines()
            linenum = 0
            for line in Lines:
                linenum = linenum + 1
                if linenum == 1:
                    print("OS Name = " + line)
                if linenum == 2:
                    print("Version = " + line)
                if linenum == 3:
                    print("Times Started Up = " + line)
    if command.lower() == "changeosname":
        if value:
            with open(pyloc + "\SYSSTATS.cfg") as f:
                Lines = f.readlines()
                linenum = 0
                for line in Lines:
                    linenum = linenum + 1
                    if linenum == 1:
                        osn = line
                    if linenum == 2:
                        ver = line
                    if linenum == 3:
                        tsu = line
            with open(pyloc + "\sysf\SYSSTATS.cfg", "w") as f:
                f.write(str(value) + "\n" + ver + tsu)

    #print(pyloc + r'\\' + dir)
    #print("Error has occured")