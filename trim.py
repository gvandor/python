#!/usr/bin/python3
import os
os.system("sudo fstrim -v /")
print ("root kész")
os.system("sudo fstrim -v /home")
print ("/home kész")
os.system("sudo fstrim -v /mnt/adat")
print ("adat kész")
print ("Kész vagyok, most kéne egy kis pálinka")
