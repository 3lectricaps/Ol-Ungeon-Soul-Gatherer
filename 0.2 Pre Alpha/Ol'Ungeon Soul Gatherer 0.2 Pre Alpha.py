# -*- coding: utf-8 -*-
import time
import math
import os

action = False
keyboardAsk = False
difficultyAsk = False

posX = 0
posY = 0

a = "o"
b = "o"
c = "o"
d = "o"
e = "o"
f = "o"
g = "o"
h = "o"
i = "o"
j = "o"
k = "o"
l = "o"
m = "█"
n = "o"
o = "o"
p = "o"
q = "o"
r = "o"
s = "o"
t = "o"
u = "o"
v = "o"
w = "o"
x = "o"
y = "o"

leftEE = "<"
rightEE = ">"
upEE = "_"
downEE = "¯"

soulEnergy = 0
maxSoulPoints = 0
soulPointsCount = 0
score = 0

maxLife = 0
lifeCount = 0

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
print("Version: 0.2")
time.sleep(1)
print()
print("State: Pre-Alpha")
time.sleep(1)
print()
print()
print("Changelog:")
time.sleep(.5)
print()
print("-Opened in normal command, the screen now is clear and dosen't show old actions.")
print()
print("-Cleared the design differnce between Soul Points, which is the new addition, and Soul Energy:")
print(" Soul Points will later be used to unleash Soul Abilities while Soul Energy is the energy used to pass levels.")
print(" Though, Soul Energy will give more Max Soul Points and increase your powers.")
print()
print("-There's a little bugfix, where if you entered a non integer value when asking for keyboard set and difficulty rate,")
print(" the game crashed. I'm happy to announce this is no longer the case!")
print()
print("-Lots of spaces between written text and such has been fixed and got more readable.")
print()
print("-Removed unused vars.")
print()
print("-Minor fixes that enhance the gameplay in general.")
print()
print("-Keep in mind that some concepts are wrote into the instructions but aren't available yet and marked as unknown actions!")
print()
time.sleep(.1)

input("New Game")

os.system('cls')

print()
print()

keyboardAsk = True

while keyboardAsk == True:
    try:
        keyboard = input("QWERTY or AZERTY? 0 for QWERTY-1 for AZERTY: ")
    except keyboard != "0" or "1":
        continue
    else:
        if keyboard == "0":
            print()
            print()
            print("How to play:")
            time.sleep(1)
            print()
            print("-Select WASD for a move then press enter.")
            keyboardAsk = False
            break
        elif keyboard == "1":
            print()
            print()
            print("How to play:")
            time.sleep(1)
            print()
            print("-Select ZQSD for a move then press enter.")
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
            lifeCount = 20
            maxSoulPoints = 15
            soulPointsCount = maxSoulPoints
            print("Difficulty: Normal")
            difficultyAsk = False
            break
        elif difficultyRate == "2":
            maxLife = 20
            lifeCount = 10
            maxSoulPoints = 20
            soulPointsCount = maxSoulPoints
            print("Difficulty: Hard")
            difficultyAsk = False
            break
    print("There are only 3 difficulty rates, so choose wisely!")
    print()

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

levelNumber = 1
roomNumber = 1

os.system('cls')

print ("~~~~~~~~~~~~~")
time.sleep(0.25)
print ("Soul Energy:", soulEnergy)
time.sleep(0.25)
print ("Level:", levelNumber)
time.sleep(0.25)
print ("Room:", roomNumber)
time.sleep(0.25)
print ("_____",upEE,"_____")
time.sleep(0.25)
print ("|",a,b,c,d,e,"|")
time.sleep(0.25)
print ("|",f,g,h,i,j,"|")
time.sleep(0.25)
print (leftEE,k,l,m,n,o,rightEE)
time.sleep(0.25)
print ("|",p,q,r,s,t,"|")
time.sleep(0.25)
print ("|",u,v,w,x,y,"|")
time.sleep(0.25)
print ("¯¯¯¯¯",downEE,"¯¯¯¯¯")
time.sleep(0.25)
print ("Life:", lifeCount,"/",maxLife)
time.sleep(0.25)
print ("SP:", soulPointsCount,"/",maxSoulPoints)
time.sleep(0.25)
print("Score:", score)
time.sleep(0.25)
print ("~~~~~~~~~~~~~")
time.sleep(0.25)
print()

inGame = True
while inGame == True:

    action = 1

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
            print ("Soul Energy:", soulEnergy)
            print ("Level:", levelNumber)
            print ("Room:", roomNumber)
            print ("_____",upEE,"_____")
            print ("|",a,b,c,d,e,"|")
            print ("|",f,g,h,i,j,"|")
            print (leftEE,k,l,m,n,o,rightEE)
            print ("|",p,q,r,s,t,"|")
            print ("|",u,v,w,x,y,"|")
            print ("¯¯¯¯¯",downEE,"¯¯¯¯¯")
            print ("Life:", lifeCount,"/",maxLife,)
            print ("SP:", soulPointsCount,"/",maxSoulPoints)
            print ("Score:", score)
            print ("~~~~~~~~~~~~~")
            print ()


    if (posY == 0 and posX > 2 and rightEE == "|") or (posY != 0 and posX > 2 and (rightEE == ">" or "&")):
        posX = 2

    elif (posY == 0 and posX < -2 and leftEE == "|") or (posY!= 0 and posX < -2 and (leftEE == "<" or "&")):
        posX = -2

    elif (posX == 0 and posY > 2 and upEE == "_") or (posX != 0 and posY > 2 and (upEE == "^" or "&")):
        posY = 2

    elif (posX == 0 and posY < -2 and downEE == "¯") or (posX != 0 and posY < -2 and (downEE == "v" or "&")):
        posY = -2
    
    elif posY == 0 and posX >= 3 and (rightEE == ">" or "&"):
        if levelNumber == 1:
            if roomNumber == 1:
                roomNumber = 2
            elif roomNumber == 2:
                roomNumber = 3
            elif roomNumber == 5:
                roomNumber = 1
        posX = -2

    elif posY == 0 and posX <= -3 and (leftEE == "<" or "&"):
        if levelNumber == 1:
            if roomNumber == 1:
                roomNumber = 5
            elif roomNumber == 2:
                roomNumber = 1
            elif roomNumber == 3:
                roomNumber = 2
        posX = 2

    elif posX == 0 and posY >= 3 and (upEE == "^" or "&"):
        if levelNumber == 1:
            if roomNumber == 2:
                roomNumber = 4
            elif roomNumber == 5:
                roomNumber = 6
        posY = -2

    elif posX == 0 and posY <= -3 and (downEE == "v" or "&"):
        if levelNumber == 1:
            if roomNumber == 4:
                roomNumber = 2
            elif roomNumber == 6:
                roomNumber = 5
        posY = 2
        
    if levelNumber == 1:
        if roomNumber == 1:
            rightEE = ">"
            leftEE = "<"
            upEE = "_"
            downEE = "¯"
        elif roomNumber == 2:
            rightEE = ">"
            leftEE = "<"
            upEE = "^"
            downEE = "¯"
        elif roomNumber == 3:
            rightEE = "|"
            leftEE = "<"
            upEE = "_"
            downEE = "¯"
        elif roomNumber == 4:
            rightEE = "|"
            leftEE = "|"
            upEE = "_"
            downEE = "v"
        elif roomNumber == 5:
            rightEE = ">"
            leftEE = "|"
            upEE = "^"
            downEE = "¯"
        elif roomNumber == 6:
            rightEE = "|"
            leftEE = "|"
            upEE = "&"
            downEE = "v"

    if posX == 0 and posY == 0:
        m = "█"
    else:
        m = "o"

    if posX == 1 and posY == 0:
        n = "█"
    else:
        n = "o"
        
    if posX == 2 and posY == 0:
        o = "█"
    else:
        o = "o"
        
    if posX == -1 and posY == 0:
        l = "█"
    else:
        l = "o"
    
    if posX == -2 and posY == 0:
        k = "█"
    else:
        k = "o"
        
    if posX == 0 and posY == 1:
        h = "█"
    else:
        h = "o"

    if posX == 1 and posY == 1:
        i = "█"
    else:
        i = "o"
        
    if posX == 2 and posY == 1:
        j = "█"
    else:
        j = "o"
        
    if posX == -1 and posY == 1:
        g = "█"
    else:
        g = "o"
    
    if posX == -2 and posY == 1:
        f = "█"
    else:
        f = "o"
        
    if posX == 0 and posY == 2:
        c = "█"
    else:
        c = "o"

    if posX == 1 and posY == 2:
        d = "█"
    else:
        d = "o"
        
    if posX == 2 and posY == 2:
        e = "█"
    else:
        e = "o"
        
    if posX == -1 and posY == 2:
        b = "█"
    else:
        b = "o"
    
    if posX == -2 and posY == 2:
        a = "█"
    else:
        a = "o"
        
    if posX == 0 and posY == -1:
        r = "█"
    else:
        r = "o"

    if posX == 1 and posY == -1:
        s = "█"
    else:
        s = "o"
        
    if posX == 2 and posY == -1:
        t = "█"
    else:
        t = "o"
        
    if posX == -1 and posY == -1:
        q = "█"
    else:
        q = "o"
    
    if posX == -2 and posY == -1:
        p = "█"
    else:
        p = "o"
        
    if posX == 0 and posY == -2:
        w = "█"
    else:
        w = "o"

    if posX == 1 and posY == -2:
        x = "█"
    else:
        x = "o"
        
    if posX == 2 and posY == -2:
        y = "█"
    else:
        y = "o"
        
    if posX == -1 and posY == -2:
        v = "█"
    else:
        v = "o"
    
    if posX == -2 and posY == -2:
        u = "█"
    else:
        u = "o"

    os.system('cls')

    print ("~~~~~~~~~~~~~")
    print ("Soul Energy:", soulEnergy)
    print ("Level:", levelNumber)
    print ("Room:", roomNumber)
    print ("_____",upEE,"_____")
    print ("|",a,b,c,d,e,"|")
    print ("|",f,g,h,i,j,"|")
    print (leftEE,k,l,m,n,o,rightEE)
    print ("|",p,q,r,s,t,"|")
    print ("|",u,v,w,x,y,"|")
    print ("¯¯¯¯¯",downEE,"¯¯¯¯¯")
    print ("Life:", lifeCount,"/",maxLife,)
    print ("SP:", soulPointsCount,"/",maxSoulPoints)
    print ("Score:", score)
    print ("~~~~~~~~~~~~~")
    print ()
