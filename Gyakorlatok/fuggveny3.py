#!/usr/bin/python3
#-*- coding:utf-8 -*-
# fuggveny3.py

# Kiírja az argumentum értékét
def mutat(v):       # egy paraméter
    print(v)
    return          # nincs v.térési érték

# Mindig 10-et ír ki
def c10():          # nincs paraméter
    print(10)
    #return
    # nincs v.térési érték és a return sem fontos

# Tesztelés
mutat(3.14)     # "belül" van a print()
c10()           # "belül" van a print()

a= c10()
print(a)
print(type(mutat))
#Sok programnyelvben, ha egy függvénynek nincs visszatérési értéke, akkor az egy értékadás jobb oldalán nem szerepelhet, mert az értelmező vagy fordító hibát fog jelezni. Esetünkben az a= c10() kódra mégsem panaszkodik a Python-értelmező. Azért nem, mert ez az értékadás érvényesnek minősül; ugyanis a Pythonban minden függvénynek lesz visszatérési értéke. Ha a programozó nem határozz meg ilyent, akkor az értelmező egy speciális értéket, a None-t adatja vissza a rutinnal. Ez nem azt jelenti, hogy semmit sem adott vissza a függvény, mert a None az az ún. üres objektum, ami még bizonyos tulajdonságokkal is rendelkezik, azon túl, hogy létezik a számítógép memóriájában. Gyakran fogunk vele találkozni a későbbiekben.
