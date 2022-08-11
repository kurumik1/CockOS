#imports
import os
import time

pyloc = os.getcwd()
filesystemlocation = pyloc + os.path.normpath("/")
curdir = "FileSys/"
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
                        else:
                            print(inputCock)
                    if cummand == "WAIT":
                        time.sleep(int(inputCock))
                    if cummand == "VARINPUT":
                        cockinp = input("CockAssEmbly Input: ")
                    if cummand == "RESPONDINPUT":
                        if not cockinp == inputCock:
                            ignorenextline = True
                else:
                    ignorenextline = False
            except:
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
            File = pyloc + r"\\" + dir + "\\" + value
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
    #print(pyloc + r'\\' + dir)
    #print("Error has occured")
