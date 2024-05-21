#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# függvények2.py

# Lineáris függvény
def lini(x):        # egy paraméter
    y= 3*x + 1
    return y        # egy v.térési érték

# Másodfokú fgv
def másodf(x):      # egy paraméter
    return x*x-4    # egy v.térési érték

# Egyidejűleg számol két fgv.-t
def máli(x):                    # egy paraméter
    return lini(x), másodf(x)   # két v.térési érték

# Párhuzamos egyenesek
def ugrás(x,c):         # két paraméter
    return 3*x + c      # egy v.térési érték

# A fenti fgv-ek tesztelése
print( másodf(0), másodf(2) )

y1,y2 = máli(3)
print( y1, y2)

print( ugrás(1,1), ugrás(1,2), ugrás(2,2) )
# A kimenet:
# -4 0
# 10 5
# 4 5 8
#Az itteni függvények belsejében használt x,y,c változók a függvényeken kívüli utasítások számára láthatatlanok, ún. lokális változók. Ezen változók a függvény végrehajtása során jönnek létre és annak visszatérése után megszűnnek létezni, és ez minden újabb híváskor újra és újra így fog lejátszódni.


