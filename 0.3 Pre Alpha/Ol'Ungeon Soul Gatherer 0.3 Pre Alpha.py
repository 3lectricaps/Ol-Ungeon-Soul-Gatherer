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
time.sleep (.1)
print("Version: 0.3")
time.sleep(1)
print()
print("State: Pre-Alpha")
time.sleep(1)
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
    except menu != "0" or "1" or "2" or "3":
        continue
    else:
        if menu == "0":
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
                            print("-Select W, A, S or D for a move then press enter.")
                            keyboardAsk = False
                            break
                        elif keyboard == "1":
                            print()
                            print()
                            print("How to play:")
                            time.sleep(1)
                            print()
                            print("-Select Z, Q, S or D for a move then press enter.")
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
                print("-K is a Keystone, it open doors.")
                time.sleep(1)
                print()
                print("-D is a door, it's blocked without a key.")
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
            print("Version: 0.3")
            print()
            print("State: Pre-Alpha")
            print()
            print()
            print("Changelog:")
            print()
            print("-As you can see, I added a Menu! There are four options from there.")
            print(" The Continue option isn't available yet, though...")
            print(" But don't worry! It will be used when my work on save files will be done!")
            print()
            print("-Hud display has been redesigned! It's way more neato now.")
            print(" I used space dots for environement and put on double borders.")
            print()
            print("-You can now choose to skip the intro if you open a New Game.")
            print()
            print("-Added a text bar which will have more uses later.")
            print()
            print("-Added new dungeon elements! Keystone and Locked Door.")
            print()
            print("-I do know it's minor, but I added notes for most of the useful vars.")
            print(" Just in case if you guys want to check the code (or if I'm lost, haha)!")
            print(" I'm probably going to add more notes in it, so I'll keep you informed.")
            print()
            print("-Keep in mind that some concepts are wrote into the instructions but aren't available yet and marked as unknown actions!")
            print()
            print()
            input("Press Start to return")
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
    time.sleep(1)

time.sleep(2.5)
print()
print("Well?")
time.sleep(1)
print("What are you waiting for?!")
time.sleep(2.5)
print("Go and beat everyone here to show these guys who's the Boss!")
time.sleep(1)
print()
input("Press Start")

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

    action = 1
    textBar = ""
    talk = False

    while action == 1:
        try:
            choose = input("Action: ")
        except (keyboard == "0" and choose != d or a or w or s) or (keyboard == "1" and choose != d or q or z or s):
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
                if key1 == True:
                    door1Unlock = True
                if door1Unlock == True:
                    talk = True
                    textBar = "Door unlocked!"
                    roomNumber = 6
                    posY = -2
                else:
                    talk = True
                    textBar = "You need a Keystone to open this door!"
                    posY = 2
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
        c = "█"
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
        y = "█"
    else:
        y = "·"
        
    if posX == -1 and posY == -2:
        v = "█"
    else:
        v = "·"
    
    if posX == -2 and posY == -2:
        u = "█"
    else:
        u = "·"

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
