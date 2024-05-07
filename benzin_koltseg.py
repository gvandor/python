#!/usr/bin/python3
#-*- coding:utf-8 -*-
# benzin_koltseg.py
# s=távolság, b=benzin ára f=fajlagos fogyasztás 100 km-en, 
#c=költség
def cost (s,b): #költség = b*(s*f/100)
    f=5.5
    c=b*(s*f/100)
    return c
print("Az út költsége: ",cost(60,641))
