__author__ = "grammaticus"
__date__ = "$Mar 21, 2012 10:56:29 AM$"

import math

#Given acceleration and Proper Time
def tObj1(a, pTime, C):
    return (C / a) * math.sinh(a * pTime / C)

def tObj2(ev, mr, a, C):
    return (C / a) * math.sinh((ev / C) * math.log(mr))

#Given acceleration and distance
def tObj3(a, d, C):
    return math.sqrt(math.pow(d / C, 2) + 2 * d / a)

#Given acceleration and Proper Time
def tDist1(a, pTime, C):
    return (math.pow(C, 2) / a) * (math.cosh(a * pTime / C)-1)

#Given exhaust velocity, acceleration, and proper time
def tDist2(ev, mr, a, C):
    return (math.pow(C, 2)/a)*(math.cosh((ev/C)*math.log(mr)-1))

#Given acceleration and Terra Time
def tDist3(a, tTime, C):
    return (math.pow(C, 2)/a)*(math.sqrt(1 +math.pow(a*tTime/C, 2))-1)

#Given acceleration and Proper Time
def tVFin1(a, pTime, C):
    return C * math.tanh(a * pTime / C)

#Given acceleration and Terra Time
def tVFin2(a, tTime, C):
    return (a * tTime) / math.sqrt(1 + math.pow(a * tTime / C, 2))

if __name__ == "__main__":
    print "Please run 'python main.py'"
