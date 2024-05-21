#!/usr/bin/python3
#-*- coding:utf-8 -*-
# polinom.py

# Kiszámítja a megadott helyen

def polinom(x):

    a4= 3
    a3= 0
    a2= 2
    a1= 5
    a0= -1
    return a4*x**4 + a3*x**3 + a2*x**2 + a1*x + a0

r= polinom(1)
print(r)

print(polinom(0))
print(polinom(10))
#A függvényeket még azok első meghívása előtt definiálni kell, ezért a programfájlban rendszerint előre csoportosítjuk őket.

#A későbbi fejezetekben lesz csak szó az ún. elágazásokról, ahol bizonyos feltételek teljesülése vagy nem teljesülése esetén más-más utasításcsoportokkal folytatódik a függvényblokk végrehajtása: ekkor igény szerint több return utasítást is elhelyezhetünk a függvényen belül.

#A következő függvények3.py program két függvényt mutat be, az egyiknek egy paramétere van és nincs visszatérési értéke, a másiknak nincs sem paramétere, sem visszatérési értéke. Az utóbbiban a return utasítás önmagában szerepel. Amennyiben a visszatérési érték nélküli rutin olyan, hogy nincs benne elágazás, akkor a return utasítás el is hagyható.
