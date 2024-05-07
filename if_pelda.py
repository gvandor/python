#!/usr/bin/python3
# if_példa.py

esik= False
a= 0

if esik:
    # a blokk1 kezdete
    print(" Esik az eső")
    a= a-1
    # a blokk1 vége
else:
    # a blokk2 kezdete
    print(" Nem esik az eső")
    a= a+1
    # a blokk2 vége
print(" a=", a)

def beolvas():
    s= input("Kapok valamit? ")
    if s:
        print(s, "<--- Köszi.")
    else:
          print("Köszi a nagy semmit!")
beolvas()

def beszámol():
       ks= "..........................."
       hossz= len(ks)
       tipp= int(input("Milyen hosszú a kígyó? "))
       if tipp == hossz:
            print("Eltaláltad!")
            return
       if tipp < hossz:
            print("Nagyobb.")
       else:
            print("Kisebb.")
beszámol()  # 27 a helyes válasz.

def osztható(osztandó, osztó):
   
        msg= "Egész számot várok!"
        if  osztó != int(osztó):
            print(msg)
            #return None
        if int(osztandó) != osztandó:
            print(msg)
            #return None
        if osztó == osztandó:
            print("Megegyeznek")
            #return True Nem jöttem rá, minek a return, nélküli is működik.
        if osztó > osztandó:
            print("Nagyobb az osztó")
        else :
            print("Kisebb az osztó")
osztható(1000, 200)


