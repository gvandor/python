#!/usr/bin/python3
# figyelj a usernévre, a Documents vagy Dokumentumok nevekre!
# !!! minden mentéskor írd át a számot négy helyen
# # Utolsó mentés: március 7.-én,  száma: 26.
# 2022 augusztus 25. száma 27
import os
os.system("cd /mnt/raktar/Adatmentes/Documents/")
os.system("mkdir Documents_27")
os.system("cd ./Documents_27")
os.system("echo Adatmentés folyamatban.")
os.system("tar -czvf documents_27.tgz /mnt/adat/Documents/*")
os.system("clear")
os.system("echo Ellenőrző összeg létrehozása sha256, mindjárt kész.")
os.system("sha256sum documents_27.tgz > CHECKSUM")















