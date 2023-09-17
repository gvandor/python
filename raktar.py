#!/usr/bin/python3
#-*- coding:utf-8 -*-
# program: raktar and ufw start.
import os
os.system("sudo mount UUID=755ab626-ff19-436c-b146-bcc1e6558b5b /mnt/raktar")
os.system("sudo ufw enable")
print ("Tűzfal megy, raktar csatolva: /mnt/raktar.")
