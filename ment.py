#!/usr/bin/python3
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
            try:
                number = int(''.join(filter(str.isdigit, filename[10:])))
                if number > max_number:
                    max_number = number
            except ValueError:
                pass
    return max_number

def main():
    """
    A fő függvény.
    """
    path = "/home/gvandor/Adat/Adatmentes/Documents/"
    max_number = get_max_number(path)
    new_number = max_number + 1

    # A könyvtár létrehozása
    os.system("mkdir {}/Documents_{}".format(path, new_number))

    # A könyvtárba lépés
    os.chdir("{}/Documents_{}".format(path, new_number))

    # Az adatok mentése
    print ("Adatmentés folyamatban.")
    os.system("tar -czvf documents_{}.tgz /home/gvandor/Adat/Documents/*".format(new_number))

    # Az ellenőrző összeg létrehozása
    os.system("clear")
    print ("Ellenőrző összeg létrehozása sha256, mindjárt kész.")
    os.system("sha256sum documents_{}.tgz > CHECKSUM".format(new_number))

if __name__ == "__main__":
    main()
print ("Adatmentés kész, most jólesne egy kis barackpálinka.")




