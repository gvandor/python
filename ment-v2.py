#!/usr/bin/python3
# Ez a kód a következőképpen működik:
# A get_max_number() függvény megkeresi a megadott könyvtárban a legnagyobb számot.
# A main() függvény először megkeresi a legnagyobb számot. Ezután létrehoz egy új könyvtárat a következő formátumban: "Documents_<szám>". Ezután a könyvtárba lép, és elmenti az adatokat. Végül létrehoz egy ellenőrző összeget a tömörített fájlhoz.

print ("gvandor python kódja")
import os

def get_max_number(path):
  """
  Megkeresi a megadott könyvtárban a legnagyobb számot.

  Args:
    path: A könyvtár elérési útja.

  Returns:
    A legnagyobb szám.
  """
  max_number = 0
  for filename in os.listdir(path):
    if filename.startswith("Documents_"):
      number = int(filename[9:])
      if number > max_number:
        max_number = number
  return max_number

def main():
  """
  A fő függvény.
  """
  path = "/mnt/raktar/Adatmentes/Documents/"
  max_number = get_max_number(path)
  new_number = max_number + 1

  # A könyvtár létrehozása
  os.system("mkdir Documents_{}".format(new_number))

  # A könyvtárba lépés
  os.system("cd Documents_{}".format(new_number))

  # Az adatok mentésése
  os.system("echo Adatmentés folyamatban.")
  os.system("tar -czvf documents_{}.tgz /mnt/adat/Documents/*".format(new_number))

  # Az ellenőrző összeg létrehozása
  os.system("clear")
  os.system("echo Ellenőrző összeg létrehozása sha256, mindjárt kész.")
  os.system("sha256sum documents_{}.tgz > CHECKSUM".format(new_number))

if __name__ == "__main__":
  main()

#  Ha a kódban a get_max_number() függvényt módosítod, akkor a könyvtárak számozását is módosíthatod. Például, ha a következő kódot használod akkor a könyvtárak számozása 0-tól 99-ig fog menni.:
# def get_max_number(path):
#"""
#Megkeresi a megadott könyvtárban a legnagyobb számot.

#Args:
# path: A könyvtár elérési útja.

 # Returns:
  #  A legnagyobb szám.
 # """
#  max_number = 0
 # for filename in os.listdir(path):
 #   if filename.startswith("Documents_"):
  #    number = int(filename[9:])
  #    if number > max_number:
 #       max_number = number
 # return max_number % 100
