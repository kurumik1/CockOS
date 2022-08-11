#imports
import os
import time
import linecache
import random
import socket
import subprocess

pyloc = os.getcwd()
filesystemlocation = pyloc + os.path.normpath("/")
curdir = "FileSys\\"

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
    newtsu = int(tsu) + 1
with open(pyloc + "\SYSSTATS.cfg", "w") as f:
    f.write(osn + ver + str(newtsu))

def contains(tuple, given_char):
    for ch in tuple:
        if ch == given_char:
            return True
    return False
def readCockScript(Faile): #CockAssEmbly
    #Better than assembly.
    with open(Faile) as f:
        ignorenextline = False
        Lines = f.readlines()
        count = 0
        for line in Lines:
            count += 1
            ababs = line
            #print(ababs)
            cummand, inputCock = getcommand(ababs)
            try:
                if not ignorenextline == True:
                    if cummand == "PRINT":
                        if inputCock == "INPUT":
                            print(cockinp)
                        elif inputCock == "RANNUM":
                            print(RANDINT)
                        else:
                            print(inputCock)
                    if cummand == "WAIT":
                        time.sleep(int(inputCock))
                    if cummand == "VARINPUT":
                        cockinp = input("CockAssEmbly Input: ")
                    if cummand == "RESPONDINPUT":
                        if not cockinp == inputCock:
                            ignorenextline = True
                    if cummand == "RAND":
                        RANDINT = random.randint(1, 2147483647) #max is 32bit integer limit cuz why not
                    if cummand == "LOOP": #this took a while asdasfdksjdglkfsdjgl
                        nval = inputCock.replace(",", "")
                        #print(nval)
                        tuplet = tuple(nval)
                        counte = 0
                        #print(tuplet)
                        while True:
                            for lain in Lines:
                                count += 1
                                if contains(tuplet, str(count)):
                                    lain = linecache.getline(Faile, count)
                                    cuemmandlain, inputCeock = getcommand(lain)
                                    if cuemmandlain == "PRINT":
                                        if inputCeock == "INPUT":
                                            print(cockinp)
                                        else:
                                            print(inputCeock)
                                    if cuemmandlain == "WAIT":
                                        time.sleep(int(inputCeock))
                                    if cuemmandlain == "VARINPUT":
                                        cockinp = input("CockAssEmbly Input: ")
                                    if cuemmandlain == "RESPONDINPUT":
                                        if not cockinp == inputCeock:
                                            ignorenextline = True
                            count = 0
                else:
                    ignorenextline = False
            except Exception as er:
                print(er)
                print("CockAssEmbly Error At line" + str(count))
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
while True:
    val = input(curdir + " -> ")
    command, value = getcommand(val)
    if command == "setdir":
        if not value == "error":
            dir = value
            ACTUALdir = pyloc + dir
            curdir = dir
        else:
            print("Enter a directory after setdir")
    if command == "open":
        if not value == "error":
            print(dir)
            File = pyloc + "\\" + dir + "\\" + value
            filename, fext = os.path.splitext(File)
            if fext == ".cok":
                readCockScript(File)
            if fext == ".txt":
                with open(File) as f:
                    lines = f.readlines()
                print(lines)
        else:
            print("Enter a file name")
    if command == "write":
        if not value == "error":
            File = pyloc + r"\\" + dir + "\\" + value
            filename, fext = os.path.splitext(File)
            if fext == ".txt":
                with open(File, 'w') as f:
                    f.write(input("What to write? "))
                print(lines)
        else:
            print("Enter a file name")
    if command == "dircont":
        with os.scandir(pyloc + r"\\" + dir) as entries:
            print("Contents in directory " + dir)
            for entry in entries:
                print(entry.name)
    if command == "getip":
        print(socket.gethostbyname(socket.gethostname()))
    if command == "repeat":
        if value:
            print(value)
    if command == "sex":
        print("*sex noises*") #haha get it its sex so its fune
    if command == "systemstats":
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
    if command == "ChangeOsName":
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
            with open(pyloc + "\SYSSTATS.cfg", "w") as f:
                f.write(str(value) + "\n" + ver + tsu)

    #print(pyloc + r'\\' + dir)
    #print("Error has occured")