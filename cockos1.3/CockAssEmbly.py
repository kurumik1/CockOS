import os
import time
import linecache
import random
import socket
import subprocess
import sys #guys1!! do not  replas the y in sys with u!!!!!
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
                    if cummand.upper() == "PRINT":
                        ohlordthatsabigasscock = inputCock.replace("_", " ") #no _?
                        if inputCock.upper() == "INPUT":
                            ohlordthatsabigasscock = ohlordthatsabigasscock.replace("INPUT", cockinp)
                        elif inputCock.upper() == "RANNUM":
                            ohlordthatsabigasscock = ohlordthatsabigasscock.replace("RANNUM", RANDINT)
                        print(ohlordthatsabigasscock)
                    if cummand.upper() == "WAIT":
                        time.sleep(int(inputCock))
                    if cummand.upper() == "VARINPUT":
                        cockinp = input("CockAssEmbly Input: ")
                    if cummand.upper() == "RESPONDINPUT":
                        if not cockinp == inputCock:
                            ignorenextline = True
                    if cummand.upper() == "RAND":
                        RANDINT = random.randint(1, 2147483647) #max is 32bit integer limit cuz why not
                    if cummand.upper() == "LOOP": #this took a while asdasfdksjdglkfsdjgl
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
                                    if cuemmandlain.upper() == "PRINT":
                                        ohlordthatsabigasscock = inputCeock.replace("_", " ") #no _?
                                        if inputCock.upper() == "INPUT":
                                            ohlordthatsabigasscock = ohlordthatsabigasscock.replace("INPUT", cockinp)
                                        elif inputCock.upper() == "RANNUM":
                                            ohlordthatsabigasscock = ohlordthatsabigasscock.replace("RANNUM", RANDINT)
                                        print(ohlordthatsabigasscock)
                                    if cuemmandlain.upper() == "WAIT":
                                        time.sleep(int(inputCeock))
                                    if cuemmandlain.upper() == "VARINPUT":
                                        cockinp = input("CockAssEmbly Input: ")
                                    if cummand.upper() == "RAND":
                                        RANDINT = random.randint(1, 2147483647) #max is 32bit integer limit cuz why not
                                    if cuemmandlain.upper() == "RESPONDINPUT":
                                        if not cockinp == inputCeock:
                                            ignorenextline = True
                            count = 0
                else:
                    ignorenextline = False
            except Exception as er:
                print(er)
                print("CockAssEmbly Error At line" + str(count))

#Red sun, red sun over paradise
#Red sun, red sun over paradise
#Golden rays of the glorious sunshine
#Sending down such a blood-red light
#Now, the animals slowly retreat to the shadows, out of sight
#Arid winds blow across the mountains
#Giving flight to the birds of prey
#In the distance machines come to transform Eden, day by day
#Only love is with us now
#Something warm and pure
#Find the peace within ourselves
#No need for a cure
#When the wind is slow, when the fire's hot
#The vulture waits to see what rots
#Oh, how pretty, all the scenery
#This is nature's sacrifice
#When the air blows through with a brisk attack
#The reptile tail ripped from its back
#When the sun sets
#We will not forget the red sun over paradise
#Red sun