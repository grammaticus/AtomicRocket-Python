__author__ = "grammaticus"
__date__ = "$Mar 21, 2012 10:56:00 AM$"

import math

#Given acceleration and Terra Time
def pTime1(a, tTime, C):
    return (C / a) * math.asinh(a * tTime/C)

#Given acceleration and distance
def pTime2(a, d, C):
    return (C / a) * math.acosh(a * d / math.pow(C, 2) + 1)

#Given acceleration and Proper Time
def gamma1(a, pTime, C):
    return math.cosh(a * pTime / C)

#Given exhaust velocity and mass ratio
def gamma2(ev, mr, C):
    return math.cosh((ev / C) * math.log(mr))

#Given acceleration and Terra Time
def gamma3(a, tTime, C):
    return math.sqrt(1 + math.pow(a * tTime / C, 2))

#Given acceleration and distance
def gamma4(a, d, C):
    return a * d / math.pow(C, 2) + 1

if __name__ == "__main__":
    print "Please run 'python main.py'"
