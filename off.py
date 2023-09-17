#!/usr/bin/python3
#-*- coding:utf-8 -*-
# program: shutdown process
print("Kezdeményezted a rendszer leállítást!")
import os
def off():
    c= input("Biztos vagy benne?, ha igen akkor adj egy karaktert + enter, ha nem akkor csak enter ")
    if c:
        os.system ("sudo shutdown -h now")
    else:
        print ("Rendben akkor most nem. ")
off()
# ide kell egy számáló.
