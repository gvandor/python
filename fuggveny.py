#!/usr/bin/python3
#-*- coding:utf-8 -*-
# program: fugveny.py

# Az első függvényünk

def lini(x):

    y= 3*x + 1   # Ez egy lineáris függvény
    return y

print( lini(1) )
print( lini(2) )
#print( lini(10) )
print( lini(1.5) )

x1= 10
y1= lini(x1)
print(x1,y1)
# A függvényblokk minden sorát egy tabulátor pozícióval beljebb kezdtük. 
