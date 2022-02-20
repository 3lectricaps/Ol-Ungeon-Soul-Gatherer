# -*- coding: utf-8 -*-
import time
import math
import os
import sys

#gameplay vars
action = False
menuChoice = False
keyboardAsk = False
difficultyAsk = False
pause = False
pauseScroll = 0


#position vars
posX = 0
posY = 0

#screen vars
a = "·"
b = "·"
c = "·"
d = "·"
e = "·"
f = "·"
g = "·"
h = "·"
i = "·"
j = "·"
k = "·"
l = "·"
m = "█"
n = "·"
o = "·"
p = "·"
q = "·"
r = "·"
s = "·"
t = "·"
u = "·"
v = "·"
w = "·"
x = "·"
y = "·"
leftEE = "<"
rightEE = ">"
upEE = "═"
downEE = "═"

#level and room vars
levelNumber = 1
roomNumber = 1

#dungeon elements vars
key1 = False
door1Unlock = False
chest1 = False
soul1 = False
soul2 = False

#hud info vars
maxLife = 0
lifeCount = 0
soulEnergy = 0
maxSoulPoints = 0
soulPointsCount = 0
score = 0

#textbar vars
talk = False
textBar = ""



time.sleep(1)
print()
print()

print(" ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄     ▄▀▄▄▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄")
print("█   █    ▐  █ ▐  ▄▀   ▐ █    █     █ █    ▌ █      █ █  █ ▀  █ ▐  ▄▀   ▐")
print("▐  █        █   █▄▄▄▄▄  ▐    █     ▐ █      █      █ ▐  █    █   █▄▄▄▄▄ ")
print("  █   ▄    █    █    ▌      █        █      ▀▄    ▄▀   █    █    █    ▌ ")
print("   ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄▀   ▀▀▀▀   ▄▀   ▄▀    ▄▀▄▄▄▄  ")
print("         ▀     █    ▐     █        █     ▐           █    █     █    ▐  ")
print("               ▐          ▐        ▐                 ▐    ▐     ▐       ")

time.sleep(1)
print()
print()

print(" ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄       ")
print("█    █  ▐ █      █      ")
print("▐   █     █      █      ")
print("   █      ▀▄    ▄▀      ")
print(" ▄▀         ▀▀▀▀  ▄ ▄ ▄ ")
print("█                       ")
print("▐                       ")

time.sleep(1)
print()
print()

print(" ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▄ ")
time.sleep(.25)
print("█      █ █    █   █   █    █ █  █ █ █ █        ▐  ▄▀   ▐ █      █ █  █ █ █ ")
time.sleep(.25)
print("█      █ ▐    █   ▐  █    █  ▐  █  ▀█ █    ▀▄▄   █▄▄▄▄▄  █      █ ▐  █  ▀█ ")
time.sleep(.25)
print("▀▄    ▄▀     █      █    █     █   █  █     █ █  █    ▌  ▀▄    ▄▀   █   █  ")
time.sleep(.25)
print("  ▀▀▀▀     ▄▀▄▄▄▄▄▄▀ ▀▄▄▄▄▀  ▄▀   █   ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄     ▀▀▀▀   ▄▀   █   ")
time.sleep(.25)
print("           █                 █    ▐   ▐         █    ▐            █    ▐   ")
time.sleep(.25)
print("           ▐                 ▐                  ▐                 ▐        ")

time.sleep(1)
print()
print()

print(" ▄▀▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄                                           ")
print("█ █   ▐ █      █ █   █    █ █    █                                            ")
print("   ▀▄   █      █ ▐  █    █  ▐    █                                            ")
print("▀▄   █  ▀▄    ▄▀   █    █       █                                             ")
print(" █▀▀▀     ▀▀▀▀      ▀▄▄▄▄▀    ▄▀▄▄▄▄▄▄▀                                       ")
print(" ▐                            █                                               ")
print("                              ▐                                               ")
time.sleep(.5)
print(" ▄▀▀▀▀▄    ▄▀▀█▄   ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ ")
print("█         ▐ ▄▀ ▀▄ █    █  ▐ █  █   ▄▀ ▐  ▄▀   ▐ █   █   █ ▐  ▄▀   ▐ █   █   █ ")
print("█    ▀▄▄    █▄▄▄█ ▐   █     ▐  █▄▄▄█    █▄▄▄▄▄  ▐  █▀▀█▀    █▄▄▄▄▄  ▐  █▀▀█▀  ")
print("█     █ █  ▄▀   █    █         █   █    █    ▌   ▄▀    █    █    ▌   ▄▀    █  ")
print("▐▀▄▄▄▄▀ ▐ █   ▄▀   ▄▀         ▄▀  ▄▀   ▄▀▄▄▄▄   █     █    ▄▀▄▄▄▄   █     █   ")
print("▐         ▐   ▐   █          █   █     █    ▐   ▐     ▐    █    ▐   ▐     ▐   ")
print("                  ▐          ▐   ▐     ▐                   ▐                  ")

time.sleep(1)
print()
print("Hello, and welcome to Ol'Ungeon : Soul Gatherer!")
time.sleep(.1)
print("Made by Xenosyx")
time.sleep(.1)
print()
print()
input("Press Any Button")

os.system('cls')

menuChoice = True

while menuChoice == True:
    try:
        os.system('cls')
        print()
        
        print("           ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄          ")
        print("          █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █   █    █          ")
        print("          ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █           ")
        print("            █    █    █    ▌    █   █    █    █            ")
        print("▄ ▄ ▄ ▄ ▄ ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀ ▄ ▄ ▄ ▄ ▄ ")
        print("          █    █     █    ▐   █    ▐                       ")
        print("          ▐    ▐     ▐        ▐                            ")
        
        print()
        menu = input("0 for New Game - 1 for Continue - 2 for Changelog - 3 to Quit: ")
        print()
    except menu != "0" or "" or "1" or "2" or "3":
        continue
    else:
        if menu == "0" or "":
            os.system('cls')
            
            print()

            print("           ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄          ")
            print("          █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █   █    █          ")
            print("          ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █           ")
            print("            █    █    █    ▌    █   █    █    █            ")
            print("▄ ▄ ▄ ▄ ▄ ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀ ▄ ▄ ▄ ▄ ▄ ")
            print("          █    █     █    ▐   █    ▐                       ")
            print("          ▐    ▐     ▐        ▐                            ")

            print()
            skipText = input("Press 1 to skip most of the text. Put anything else to not skip: ")
            if skipText == "1":
                os.system('cls')
                print()

                print("           ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄          ")
                print("          █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █   █    █          ")
                print("          ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █           ")
                print("            █    █    █    ▌    █   █    █    █            ")
                print("▄ ▄ ▄ ▄ ▄ ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀ ▄ ▄ ▄ ▄ ▄ ")
                print("          █    █     █    ▐   █    ▐                       ")
                print("          ▐    ▐     ▐        ▐                            ")
                
                keyboardAsk = True

                while keyboardAsk == True:
                    try:
                        print()
                        keyboard = input("QWERTY or AZERTY? 0 for QWERTY - 1 for AZERTY: ")
                    except keyboard != "0" or "1":
                        continue
                    else:
                        if keyboard == "0":
                            print()
                            print("QWERTY Set")
                            keyboardAsk = False
                            break
                        elif keyboard == "1":
                            print()
                            print("AZERTY Set")
                            keyboardAsk = False
                            break
                    print()
                    print("What's your keyboard's set?")

                print()

                difficultyAsk = True

                while difficultyAsk == True:
                    
                    try:
                        difficultyRate = input("Difficulty Rate? Choose wisely! 0.Easy - 1.Normal - 2.Hard: ")
                    except difficultyRate != "0" or "1" or "2":
                        continue
                    else:
                        print()
                        if difficultyRate == "0":
                            maxLife = 50
                            lifeCount = maxLife
                            maxSoulPoints = 20
                            soulPointsCount = maxSoulPoints
                            print("Difficulty: Easy")
                            difficultyAsk = False
                            break
                        elif difficultyRate == "1":
                            maxLife = 25
                            lifeCount = maxLife
                            maxSoulPoints = 15
                            soulPointsCount = maxSoulPoints
                            print("Difficulty: Normal")
                            difficultyAsk = False
                            break
                        elif difficultyRate == "2":
                            maxLife = 20
                            lifeCount = maxLife
                            maxSoulPoints = 20
                            soulPointsCount = maxSoulPoints
                            print("Difficulty: Hard")
                            difficultyAsk = False
                            break
                    print("There are only 3 difficulty rates, so choose wisely!")
                    print()
            else:
                os.system('cls')
                print()

                print("           ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄          ")
                print("          █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █   █    █          ")
                print("          ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █           ")
                print("            █    █    █    ▌    █   █    █    █            ")
                print("▄ ▄ ▄ ▄ ▄ ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀ ▄ ▄ ▄ ▄ ▄ ")
                print("          █    █     █    ▐   █    ▐                       ")
                print("          ▐    ▐     ▐        ▐                            ")
                
                keyboardAsk = True

                while keyboardAsk == True:
                    try:
                        print()
                        keyboard = input("QWERTY or AZERTY? 0 for QWERTY - 1 for AZERTY: ")
                    except keyboard != "0" or "1":
                        continue
                    else:
                        if keyboard == "0":
                            print()
                            print()
                            print("How to play:")
                            time.sleep(1)
                            print()
                            print("-Select W, A, S or D for a move then press Enter.")
                            keyboardAsk = False
                            break
                        elif keyboard == "1":
                            print()
                            print()
                            print("How to play:")
                            time.sleep(1)
                            print()
                            print("-Select Z, Q, S or D for a move then press Enter.")
                            keyboardAsk = False
                            break
                        print()
                        print("What's your keyboard's set?")
                        print()

                time.sleep(1)
                print()
                print("-Select E for Equipement.")
                time.sleep(1)
                print()
                print("-Select R for SoulAbility.")
                time.sleep(1)
                print()
                print("-Select Enter or P to Pause the Game.")
                time.sleep(2.5)
                print()
                print()
                print("Dungeon Instructions:")
                time.sleep(2.5)
                print()
                print("-You are yourself stuck in endless caves and dungeons.")
                time.sleep(1)
                print(" You'll have to finish all the levels to get out.")
                time.sleep(1)
                print(" In order to do that, you have to travel through rooms,")
                time.sleep(1)
                print(" and gather enough soul energy in soul chests to get to the next level.")
                time.sleep(1)
                print()
                print("-There will be ennemies blocking your way to the next room/level...")
                time.sleep(1)
                print(" No need to worry, though!")
                time.sleep(1)
                print(" You are a Soul Gatherer! A living entity allowed to control Soul Energy!")
                time.sleep(1)
                print(" But even like this, you will need some equipement to defend yourself.")
                time.sleep(1)
                print(" Throughout your gameplay through the dungeons...")
                time.sleep(1)
                print(" You're gonna find plenty of ressources! So don't forget to explore!")
                time.sleep(2.5)
                print()
                print()
                print("-Elements:")
                time.sleep(2.5)
                print()
                print("-█ is the player.")
                time.sleep(1)
                print()
                print("-K is a Keystone, it open doors or chests.")
                time.sleep(1)
                print()
                print("-D is a door, it's blocked without a special item.")
                time.sleep(1)
                print()
                print("-C is a Soul Chest. You can get Items and Soul Energy in it.")
                time.sleep(1)
                print()
                print("-S is a Soul. You can gather it to get Soul Energy and more Max Soul Points.")
                time.sleep(2.5)
                print()
                print()

                difficultyAsk = True

                while difficultyAsk == True:
                    try:
                        difficultyRate = input("Difficulty Rate? Choose wisely! 0.Easy - 1.Normal - 2.Hard: ")
                    except difficultyRate != "0" or "1" or "2":
                        continue
                    else:
                        print()
                        if difficultyRate == "0":
                            maxLife = 50
                            lifeCount = maxLife
                            maxSoulPoints = 20
                            soulPointsCount = maxSoulPoints
                            print("Difficulty: Easy")
                            difficultyAsk = False
                            break
                        elif difficultyRate == "1":
                            maxLife = 25
                            lifeCount = maxLife
                            maxSoulPoints = 15
                            soulPointsCount = maxSoulPoints
                            print("Difficulty: Normal")
                            difficultyAsk = False
                            break
                        elif difficultyRate == "2":
                            maxLife = 20
                            lifeCount = maxLife
                            maxSoulPoints = 20
                            soulPointsCount = maxSoulPoints
                            print("Difficulty: Hard")
                            difficultyAsk = False
                            break
                    print("There are only 3 difficulty rates, so choose wisely!")
                    print()
            menuChoice = False
            break

        elif menu == "1":
            os.system('cls')
            print()

            print("           ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄          ")
            print("          █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █   █    █          ")
            print("          ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █           ")
            print("            █    █    █    ▌    █   █    █    █            ")
            print("▄ ▄ ▄ ▄ ▄ ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀ ▄ ▄ ▄ ▄ ▄ ")
            print("          █    █     █    ▐   █    ▐                       ")
            print("          ▐    ▐     ▐        ▐                            ")

            print()
            print("Not available yet.")
            time.sleep(1)
            continue
        elif menu == "2":
            os.system('cls')
            print()

            print("           ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄          ")
            print("          █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █   █    █          ")
            print("          ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █           ")
            print("            █    █    █    ▌    █   █    █    █            ")
            print("▄ ▄ ▄ ▄ ▄ ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀ ▄ ▄ ▄ ▄ ▄ ")
            print("          █    █     █    ▐   █    ▐                       ")
            print("          ▐    ▐     ▐        ▐                            ")

            print()
            print("Credits:")
            print()
            print("-Djemaï Ayman AKA Xenosyx")
            print()
            print()
            print("Version: 0.4")
            print()
            print("State: Pre-Alpha")
            print()
            print()
            print("Changelog:")
            print()
            print("-I now added a Pause Menu! The Saving and Loading options aren't available yet, but everything else works.")
            print()
            print("-Bugfix: textbar dosen't repeat if the door has already been unlocked anymore.")
            print()
            print("-Added new Dungeon Elements! Soul Chest and Soul.")
            print()
            print("-Keep in mind that some concepts are wrote into the instructions but aren't available yet and marked as unknown actions!")
            print()
            print()
            input("Press Enter to return")
            continue
        elif menu == "3":
            os.system('cls')
            print()

            print("           ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄          ")
            print("          █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █   █    █          ")
            print("          ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █           ")
            print("            █    █    █    ▌    █   █    █    █            ")
            print("▄ ▄ ▄ ▄ ▄ ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀ ▄ ▄ ▄ ▄ ▄ ")
            print("          █    █     █    ▐   █    ▐                       ")
            print("          ▐    ▐     ▐        ▐                            ")

            print()
            sureToQuit = input("Are you sure? Press 1 to quit and anything else to not: ")
            if sureToQuit == "1":
                sys.exit()
            else:
                continue
    print("Unknown Action...")
    time.sleep(.5)

time.sleep(1)
print()
print("Well?")
time.sleep(.5)
print("What are you waiting for?!")
time.sleep(1)
print("Go and beat everyone here to show these guys who's the Boss!")
time.sleep(.5)
print()
input("Press Enter")

os.system('cls')

print ("~~~~~~~~~~~~~")
time.sleep(0.25)
print ("Soul Energy:", soulEnergy,"%")
time.sleep(0.25)
print ("Level:", levelNumber)
time.sleep(0.25)
print ("Room:", roomNumber)
time.sleep(0.25)
print ("╔════",upEE,"════╗")
time.sleep(0.25)
print ("║",a,b,c,d,e,"║")
time.sleep(0.25)
print ("║",f,g,h,i,j,"║")
time.sleep(0.25)
print (leftEE,k,l,m,n,o,rightEE)
time.sleep(0.25)
print ("║",p,q,r,s,t,"║")
time.sleep(0.25)
print ("║",u,v,w,x,y,"║")
time.sleep(0.25)
print ("╚════",downEE,"════╝")
time.sleep(0.25)
print ("Life:", lifeCount,"/",maxLife)
time.sleep(0.25)
print ("SP:", soulPointsCount,"/",maxSoulPoints)
time.sleep(0.25)
print("Score:", score)
time.sleep(0.25)
print ("~~~~~~~~~~~~~")
time.sleep(0.25)
if talk == True:
    print()
    print(textBar)
    print()
else:
    print()
    print("...")
    print()

inGame = True
while inGame == True:

    action = True
    textBar = ""
    talk = False

    while action == True:
        try:
            choose = input("Action: ")
        except (keyboard == "0" and choose != "d" or "a" or "w" or "s") or (keyboard == "1" and choose != "d" or "q" or "z" or "s") or (choose != "p" or ""):
            continue
        else:
            if keyboard == "0":
                if choose == "d":
                    posX += 1
                    action = 0
                    break
                elif choose == "a":
                    posX -= 1
                    action = 0
                    break
                elif choose == "w":
                    posY += 1
                    action = 0
                    break
                elif choose == "s":
                    posY -= 1
                    action = 0
                    break

            elif keyboard == "1":
                if choose == "d":
                    posX += 1
                    action = 0
                    break
                elif choose == "q":
                    posX -= 1
                    action = 0
                    break
                elif choose == "z":
                    posY += 1
                    action = 0
                    break
                elif choose == "s":
                    posY -= 1
                    action = 0
                    break
            if choose == "p" or choose == "":
                os.system('cls')
                print()
                
                print(" ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
                print("█   █   █ ▐ ▄▀ ▀▄ █   █    █ █ █   ▐ ▐  ▄▀   ▐ ")
                print("▐  █▀▀▀▀    █▄▄▄█ ▐  █    █     ▀▄     █▄▄▄▄▄  ")
                print("   █       ▄▀   █   █    █   ▀▄   █    █    ▌  ")
                print(" ▄▀       █   ▄▀     ▀▄▄▄▄▀   █▀▀▀    ▄▀▄▄▄▄   ")
                print("█         ▐   ▐               ▐       █    ▐   ")
                print("▐                                     ▐        ")

                print()
                print(">Continue<")
                print()
                print("Save")
                print()
                print("Load")
                print()
                print("Option")
                print()
                print("Quit")

                pause = True
                
                while pause == True:
                    try:
                        if pauseScroll < 0:
                            pauseScroll = 4
                        elif pauseScroll > 4:
                            pauseScroll = 0
                        os.system('cls')
                        print()

                        print(" ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
                        print("█   █   █ ▐ ▄▀ ▀▄ █   █    █ █ █   ▐ ▐  ▄▀   ▐ ")
                        print("▐  █▀▀▀▀    █▄▄▄█ ▐  █    █     ▀▄     █▄▄▄▄▄  ")
                        print("   █       ▄▀   █   █    █   ▀▄   █    █    ▌  ")
                        print(" ▄▀       █   ▄▀     ▀▄▄▄▄▀   █▀▀▀    ▄▀▄▄▄▄   ")
                        print("█         ▐   ▐               ▐       █    ▐   ")
                        print("▐                                     ▐        ")
                        
                        print()
                        if pauseScroll == 0:
                            print(">Continue<")
                            print()
                            print("Save")
                            print()
                            print("Load")
                            print()
                            print("Option")
                            print()
                            print("Quit")
                        elif pauseScroll == 1:
                            print("Continue")
                            print()
                            print(">Save<")
                            print()
                            print("Load")
                            print()
                            print("Option")
                            print()
                            print("Quit")
                        elif pauseScroll == 2:
                            print("Continue")
                            print()
                            print("Save")
                            print()
                            print(">Load<")
                            print()
                            print("Option")
                            print()
                            print("Quit")
                        elif pauseScroll == 3:
                            print("Continue")
                            print()
                            print("Save")
                            print()
                            print("Load")
                            print()
                            print(">Option<")
                            print()
                            print("Quit")
                        elif pauseScroll == 4:
                            print("Continue")
                            print()
                            print("Save")
                            print()
                            print("Load")
                            print()
                            print("Option")
                            print()
                            print(">Quit<")
                        print()
                        if keyboard == "0":
                            pauseGuide = "W to Up - S to Down - Enter to Select: "
                        elif keyboard == "1":
                            pauseGuide = "Z to Up - S to Down - Enter to Select: "
                        pauseChoice = input(pauseGuide)
                        
                    except (keyboard == "0" and pauseChoice != "w" or "s" or "") or (keyboard == "1" and pauseChoice != "z" or "s" or ""):
                        continue
                    else:
                        if pauseChoice == "":
                            if pauseScroll == 0:
                                pause = False
                                break
                            elif pauseScroll == 1:
                                os.system('cls')
                                print()

                                print(" ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
                                print("█   █   █ ▐ ▄▀ ▀▄ █   █    █ █ █   ▐ ▐  ▄▀   ▐ ")
                                print("▐  █▀▀▀▀    █▄▄▄█ ▐  █    █     ▀▄     █▄▄▄▄▄  ")
                                print("   █       ▄▀   █   █    █   ▀▄   █    █    ▌  ")
                                print(" ▄▀       █   ▄▀     ▀▄▄▄▄▀   █▀▀▀    ▄▀▄▄▄▄   ")
                                print("█         ▐   ▐               ▐       █    ▐   ")
                                print("▐                                     ▐        ")
                                
                                print()
                                print("Save not available yet")
                                time.sleep(1)
                                continue
                            elif pauseScroll == 2:
                                os.system('cls')
                                print()
                                
                                print(" ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
                                print("█   █   █ ▐ ▄▀ ▀▄ █   █    █ █ █   ▐ ▐  ▄▀   ▐ ")
                                print("▐  █▀▀▀▀    █▄▄▄█ ▐  █    █     ▀▄     █▄▄▄▄▄  ")
                                print("   █       ▄▀   █   █    █   ▀▄   █    █    ▌  ")
                                print(" ▄▀       █   ▄▀     ▀▄▄▄▄▀   █▀▀▀    ▄▀▄▄▄▄   ")
                                print("█         ▐   ▐               ▐       █    ▐   ")
                                print("▐                                     ▐        ")

                                print()
                                print("Load not available yet")
                                time.sleep(1)
                            elif pauseScroll == 3:
                                
                                keyboardAsk = True
                                
                                while keyboardAsk == True:
                                    try:
                                        os.system('cls')
                                        print()

                                        print(" ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
                                        print("█   █   █ ▐ ▄▀ ▀▄ █   █    █ █ █   ▐ ▐  ▄▀   ▐ ")
                                        print("▐  █▀▀▀▀    █▄▄▄█ ▐  █    █     ▀▄     █▄▄▄▄▄  ")
                                        print("   █       ▄▀   █   █    █   ▀▄   █    █    ▌  ")
                                        print(" ▄▀       █   ▄▀     ▀▄▄▄▄▀   █▀▀▀    ▄▀▄▄▄▄   ")
                                        print("█         ▐   ▐               ▐       █    ▐   ")
                                        print("▐                                     ▐        ")
                                        
                                        print()
                                        keyboard = input("QWERTY or AZERTY? 0 for QWERTY - 1 for AZERTY: ")
                                    except keyboard != "0" or "1":
                                        continue
                                    else:
                                        if keyboard == "0":
                                            print()
                                            print("QWERTY Set")
                                            pauseGuide = "W to Up - S to Down - Enter to Select"
                                            time.sleep(1)
                                            keyboardAsk = False
                                            break
                                        elif keyboard == "1":
                                            print()
                                            print("AZERTY Set")
                                            pauseGuide = "Z to Up - S to Down - Enter to Select"
                                            time.sleep(1)
                                            keyboardAsk = False
                                            break
                                    print()
                                    print("What's your keyboard's set?")
                            elif pauseScroll == 4:
                                os.system('cls')
                                print()
                                
                                print(" ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
                                print("█   █   █ ▐ ▄▀ ▀▄ █   █    █ █ █   ▐ ▐  ▄▀   ▐ ")
                                print("▐  █▀▀▀▀    █▄▄▄█ ▐  █    █     ▀▄     █▄▄▄▄▄  ")
                                print("   █       ▄▀   █   █    █   ▀▄   █    █    ▌  ")
                                print(" ▄▀       █   ▄▀     ▀▄▄▄▄▀   █▀▀▀    ▄▀▄▄▄▄   ")
                                print("█         ▐   ▐               ▐       █    ▐   ")
                                print("▐                                     ▐        ")

                                print()
                                sureToQuit = input("Are you sure? Press 1 to quit and anything else to not: ")
                                if sureToQuit == "1":
                                    sys.exit()
                                else:
                                    continue
                        elif (keyboard == "0" and pauseChoice == "w") or (keyboard == "1" and pauseChoice == "z"):
                            pauseScroll -= 1
                        elif pauseChoice == "s":
                            pauseScroll += 1
                        else:
                            os.system('cls')
                            print()

                            print(" ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
                            print("█   █   █ ▐ ▄▀ ▀▄ █   █    █ █ █   ▐ ▐  ▄▀   ▐ ")
                            print("▐  █▀▀▀▀    █▄▄▄█ ▐  █    █     ▀▄     █▄▄▄▄▄  ")
                            print("   █       ▄▀   █   █    █   ▀▄   █    █    ▌  ")
                            print(" ▄▀       █   ▄▀     ▀▄▄▄▄▀   █▀▀▀    ▄▀▄▄▄▄   ")
                            print("█         ▐   ▐               ▐       █    ▐   ")
                            print("▐                                     ▐        ")

                            print()
                            print("Unknown Action...")
                            time.sleep(.5)
                os.system('cls')
                print ("~~~~~~~~~~~~~")
                print ("Soul Energy:", soulEnergy,"%")
                print ("Level:", levelNumber)
                print ("Room:", roomNumber)
                print ("╔════",upEE,"════╗")
                print ("║",a,b,c,d,e,"║")
                print ("║",f,g,h,i,j,"║")
                print (leftEE,k,l,m,n,o,rightEE)
                print ("║",p,q,r,s,t,"║")
                print ("║",u,v,w,x,y,"║")
                print ("╚════",downEE,"════╝")
                print ("Life:", lifeCount,"/",maxLife,)
                print ("SP:", soulPointsCount,"/",maxSoulPoints)
                print ("Score:", score)
                print ("~~~~~~~~~~~~~")
                if talk == True:
                    print()
                    print(textBar)
                    print()
                else:
                    print()
                    print("...")
                    print()
                continue
            if (keyboard == "0" and choose != "d" or "a" or "w" or "s") or (keyboard == "1" and choose != "d" or "q" or "z" or "s") or (choose != "p" or ""):
                print("Unknown Action...")
                time.sleep(.5)
            os.system('cls')
            print ("~~~~~~~~~~~~~")
            print ("Soul Energy:", soulEnergy,"%")
            print ("Level:", levelNumber)
            print ("Room:", roomNumber)
            print ("╔════",upEE,"════╗")
            print ("║",a,b,c,d,e,"║")
            print ("║",f,g,h,i,j,"║")
            print (leftEE,k,l,m,n,o,rightEE)
            print ("║",p,q,r,s,t,"║")
            print ("║",u,v,w,x,y,"║")
            print ("╚════",downEE,"════╝")
            print ("Life:", lifeCount,"/",maxLife,)
            print ("SP:", soulPointsCount,"/",maxSoulPoints)
            print ("Score:", score)
            print ("~~~~~~~~~~~~~")
            if talk == True:
                print()
                print(textBar)
                print()
            else:
                print()
                print("...")
                print()

    os.system('cls')

    if (posY == 0 and posX > 2 and rightEE == "║") or (posY != 0 and posX > 2 and (rightEE == ">" or "&" or "D")):
        posX = 2

    elif (posY == 0 and posX < -2 and leftEE == "║") or (posY!= 0 and posX < -2 and (leftEE == "<" or "&" or "D")):
        posX = -2

    elif (posX == 0 and posY > 2 and upEE == "═") or (posX != 0 and posY > 2 and (upEE == "^" or "&" or "D")):
        posY = 2

    elif (posX == 0 and posY < -2 and downEE == "═") or (posX != 0 and posY < -2 and (downEE == "v" or "&" or "D")):
        posY = -2
    
    elif posY == 0 and posX >= 3 and (rightEE == ">" or "&" or "D"):
        if levelNumber == 1:
            if roomNumber == 1:
                roomNumber = 2
                posX = -2
            elif roomNumber == 2:
                roomNumber = 3
                posX = -2
            elif roomNumber == 5:
                roomNumber = 1
                posX = -2

    elif posY == 0 and posX <= -3 and (leftEE == "<" or "&" or "D"):
        if levelNumber == 1:
            if roomNumber == 1:
                roomNumber = 5
                posX = 2
            elif roomNumber == 2:
                roomNumber = 1
                posX = 2
            elif roomNumber == 3:
                roomNumber = 2
                posX = 2

    elif posX == 0 and posY >= 3 and (upEE == "^" or "&" or "D"):
        if levelNumber == 1:
            if roomNumber == 2:
                roomNumber = 4
                posY = -2
            elif roomNumber == 5:
                if door1Unlock == False:
                    if key1 == True:
                        door1Unlock = True
                    else:
                        door1Unlock = False
                        talk = True
                        textBar = "You need a Keystone to open this door!"
                        posY = 2
                    if door1Unlock == True:
                        talk = True
                        textBar = "Door unlocked!"
                        roomNumber = 6
                        posY = -2
                else:
                    roomNumber = 6
                    posY = -2
            elif roomNumber == 6:
                talk = True
                textBar = "Level 2 isn't available yet!"
                posY = 2

    elif posX == 0 and posY <= -3 and (downEE == "v" or "&" or "D"):
        if levelNumber == 1:
            if roomNumber == 4:
                roomNumber = 2
                posY = 2
            elif roomNumber == 6:
                roomNumber = 5
                posY = 2
        
    if levelNumber == 1:
        if roomNumber == 1:
            rightEE = ">"
            leftEE = "<"
            upEE = "═"
            downEE = "═"
        elif roomNumber == 2:
            rightEE = ">"
            leftEE = "<"
            upEE = "^"
            downEE = "═"
        elif roomNumber == 3:
            rightEE = "║"
            leftEE = "<"
            upEE = "═"
            downEE = "═"
        elif roomNumber == 4:
            rightEE = "║"
            leftEE = "║"
            upEE = "═"
            downEE = "v"
        elif roomNumber == 5:
            rightEE = ">"
            leftEE = "║"
            if door1Unlock == True:
                upEE = "^"
            else:
                upEE = "D"
            downEE = "═"
        elif roomNumber == 6:
            rightEE = "║"
            leftEE = "║"
            upEE = "&"
            downEE = "v"

    if posX == 0 and posY == 0:
        m = "█"
    else:
        m = "·"

    if posX == 1 and posY == 0:
        n = "█"
    else:
        n = "·"
        
    if posX == 2 and posY == 0:
        if levelNumber == 1:
            if roomNumber == 3:
                if key1 == False:
                    o = "█"
                    talk = True
                    textBar = "Got a Keystone!"
                    key1 = True
                else:
                    o = "█"
            else:
                o = "█"
        else:
            o = "█"
    else:
        if levelNumber == 1:
            if roomNumber == 3:
                if key1 == False:
                    o = "K"
                else:
                    o = "·"
            else:
                o = "·"
        else:
            o = "·"

    if posX == -1 and posY == 0:
        l = "█"
    else:
        l = "·"
    
    if posX == -2 and posY == 0:
        k = "█"
    else:
        k = "·"
        
    if posX == 0 and posY == 1:
        h = "█"
    else:
        h = "·"

    if posX == 1 and posY == 1:
        i = "█"
    else:
        i = "·"
        
    if posX == 2 and posY == 1:
        j = "█"
    else:
        j = "·"
        
    if posX == -1 and posY == 1:
        g = "█"
    else:
        g = "·"
    
    if posX == -2 and posY == 1:
        f = "█"
    else:
        f = "·"
        
    if posX == 0 and posY == 2:
        if levelNumber == 1:
            if roomNumber == 4:
                if chest1 == False:
                    c = "█"
                    talk = True
                    textBar = "Soul Chest: Got +50% Soul Energy"
                    soulEnergy += 50
                    chest1 = True
                else:
                    c = "█"
                    talk = True
                    textBar = "Soul Chest: Already Looted!"
            else:
                c = "█"
        else:
            c = "█"
    else:
        if levelNumber == 1:
            if roomNumber == 4:
                c = "C"
            else:
                c = "·"
        else:
            c = "·"

    if posX == 1 and posY == 2:
        d = "█"
    else:
        d = "·"
        
    if posX == 2 and posY == 2:
        e = "█"
    else:
        e = "·"
        
    if posX == -1 and posY == 2:
        b = "█"
    else:
        b = "·"
    
    if posX == -2 and posY == 2:
        a = "█"
    else:
        a = "·"
        
    if posX == 0 and posY == -1:
        r = "█"
    else:
        r = "·"

    if posX == 1 and posY == -1:
        s = "█"
    else:
        s = "·"
        
    if posX == 2 and posY == -1:
        t = "█"
    else:
        t = "·"
        
    if posX == -1 and posY == -1:
        q = "█"
    else:
        q = "·"
    
    if posX == -2 and posY == -1:
        p = "█"
    else:
        p = "·"
        
    if posX == 0 and posY == -2:
        w = "█"
    else:
        w = "·"

    if posX == 1 and posY == -2:
        x = "█"
    else:
        x = "·"
        
    if posX == 2 and posY == -2:
        if levelNumber == 1:
            if roomNumber == 2:
                if soul1 == False:
                    y = "█"
                    talk = True
                    textBar = "Gathered a Soul!"
                    soulEnergy += 25
                    soul1 = True
                else:
                    y = "█"
            else:
                y = "█"
        else:
            y = "█"
    else:
        if levelNumber == 1:
            if roomNumber == 2:
                if soul1 == False:
                    y = "S"
                else:
                    y = "·"
            else:
                y = "·"
        else:
            y = "·"
        
    if posX == -1 and posY == -2:
        v = "█"
    else:
        v = "·"
    
    if posX == -2 and posY == -2:
        if levelNumber == 1:
            if roomNumber == 5:
                if soul2 == False:
                    u = "█"
                    talk = True
                    textBar = "Gathered a Soul!"
                    soulEnergy += 25
                    soul2 = True
                else:
                    u = "█"
            else:
                u = "█"
        else:
            u = "█"
    else:
        if levelNumber == 1:
            if roomNumber == 5:
                if soul2 == False:
                    u = "S"
                else:
                    u = "·"
            else:
                u = "·"
        else:
            u = "·"

    if soulEnergy > 100:
        soulEnergy = 100
    elif lifeCount > maxLife:
        lifeCount = maxLife
    elif lifeCount < 0:
        lifeCount = 0
    elif lifeCount == 0:
        lifeCount = maxLife
    elif soulPointsCount > maxSoulPoints:
        soulPointsCount = maxSoulPoints
    elif score > 9999999999:
        score = 9999999999

    print ("~~~~~~~~~~~~~")
    print ("Soul Energy:", soulEnergy,"%")
    print ("Level:", levelNumber)
    print ("Room:", roomNumber)
    print ("╔════",upEE,"════╗")
    print ("║",a,b,c,d,e,"║")
    print ("║",f,g,h,i,j,"║")
    print (leftEE,k,l,m,n,o,rightEE)
    print ("║",p,q,r,s,t,"║")
    print ("║",u,v,w,x,y,"║")
    print ("╚════",downEE,"════╝")
    print ("Life:", lifeCount,"/",maxLife,)
    print ("SP:", soulPointsCount,"/",maxSoulPoints)
    print ("Score:", score)
    print ("~~~~~~~~~~~~~")
    if talk == True:
        print()
        print(textBar)
        print()
    else:
        print()
        print("...")
        print()
