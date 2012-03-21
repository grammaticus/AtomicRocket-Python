__author__ = "grammaticus"
__date__ = "$Mar 21, 2012 10:55:29 AM$"

import math
import sys
import ship
import terra

a = -1
ev = -1
mr = -1
pTime = -1
tTime = -1
d = -1
v = -1
gamma = -1

def cAbs():
    return 299792458.0

def secs():
    return 31556926.0

def LY():
    return 9.46 * math.pow(10, 15)

def checkDone():
    choice = ""
    answer = None
    print("Do you have more information to enter?")
    choice = raw_input("[Y] or [N]: ")
    if (choice == "Y") or (choice == "y"):
        answer = True
    elif (choice == "N") or (choice == "n"):
        print("\n")
        answer = False
    else:
        print("You have entered an invalid choice")
    return answer

def getAccel():
    a = float(raw_input("Enter the acceleration in m/s^2\n(1 g = 9.81 m/s^2): "))
    return a

def getMR():
    mr = float(raw_input("Enter the mass ratio (dimensionless number): "))
    return mr

def getEV():
    ev = float(raw_input("Enter the exhaust velocity in m/s: "))
    return ev

def getPTime():
    pTime = float(raw_input("Enter the proper time in years: "))
    return pTime

def getTTime():
    tTime = float(raw_input("Enter Terra time in years: "))
    return tTime

def getDist():
    d = float(raw_input("Enter the distance in lightyears: "))
    return d

def seconds(t):
    return float(t*secs())

def years(t):
    return float(t/secs())

def meters(d):
    return float(d*LY())

def lightyears(d):
    return float(d/LY())

def psl(v, C):
    return float(v/C)

def shipMenu():
    choice = -1
    isDone = False
    global a
    global ev
    global mr
    global pTime
    print("\n** SHIP MENU **")
    while isDone == False:
        print("What information do you have about the ship?")
        print("[1] Acceleration")
        print("[2] Mass Ratio")
        print("[3] Exhaust Velocity")
        print("[4] Proper Time (ship's frame of reference")
        choice = int(raw_input("Enter your selection: "))
        if choice == 1:
            a = getAccel()
        elif choice == 2:
            mr = getMR()
        elif choice == 3:
            ev = getEV()
        elif choice == 4:
            pTime = getPTime()
        else:
            print ("You have entered an invalid choice")
        isDone = not(checkDone())


def terraMenu():
    choice = -1
    isDone = False
    global tTime
    global d

    print("** TERRA MENU **")
    while isDone != True:
        print("What information do you have about Terra?")
        print("[1] Distance")
        print("[2] Terra Time")
        print("[3] No Data")
        choice = int(raw_input("Enter your selection: "))
        if choice == 1:
            d = getDist()
        elif choice == 2:
            tTime = getTTime()
        elif choice == 3:
            break
        else:
            print ("You have entered an invalid choice")
        isDone = not(checkDone())

def calculate():
    shipMenu()
    terraMenu()
    global a
    global ev
    global mr
    global pTime
    global tTime
    global gamma
    global d
    global v
    
    C = cAbs()
    
    while (a <= 0):
        print("Error!  Acceleration must be positive")
        a = accel()

    print("** SOLUTIONS **")
    if(tTime == -1):
        tt1 = terra.tObj1(a, seconds(pTime), C)
        if (mr > 0) and (ev > 0):
            tt2 = terra.tObj2(ev, mr, a, C)
        if (d > 0):
            tt3 = terra.tObj3(a, meters(d), C)

        if tt1 > 0:
            tTime = years(tt1)
        elif tt2 > 0:
            tTime = years(tt2)
        elif tt3 > 0:
            tTime = years(tt3)
        else:
            print("Error!  You have not input enough data")
            sys.exit(1)

    print "tTime: ", round(tTime, 2)

    if (pTime == -1):
        pTime = years(ship.pTime1(a, seconds(tTime), C))

    print "pTime: ", round(pTime, 2)

    if (d == -1):
        d = lightyears(terra.tDist1(a, seconds(pTime), C))

    print "d: ", round(d, 2)

    v = psl(terra.tVFin1(a, seconds(pTime), C), C)

    print "v: ", round(v, 2)

    gamma = ship.gamma1(a, seconds(pTime), C)

    print "gamma: ", round(gamma, 2)

if __name__ == "__main__":
    calculate()