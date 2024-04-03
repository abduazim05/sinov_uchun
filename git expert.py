"""Kurtlar vodisini kichik bir maketdagi o'yini"""
from random import randint
import time
class kurtlat_vodisi:
    def __init__(self):
        self.polat = "Polat Alemdar"
        self.iskandar = "Iskandar Buyuk"
        self.polat_soul = 30
        self.iskandar_soul = 50

    def  otishmani_boshlash(self):
        print("Otishma boshlandi !!!")
        time.sleep(1)

        while self.polat_soul > 0 and self.iskandar_soul > 0:
            polat_otdi = randint(1, 20)
            iskandar_otdi = randint(1, 10)
            time.sleep(3)
            print("Iskandar otdi ")

            self.polat_soul -= iskandar_otdi
            time.sleep(3)

            if self.polat_soul < 0: # agar jon - ga teng bo'lsa
                self.polat_soul = 0
                print("Polat o'ldi")
                break
            print(f"Polatni joni: {self.polat_soul} qoldi")
            time.sleep(3)
            print("Polat otdi")
            self.iskandar_soul -= polat_otdi
            time.sleep(3)

            if self.iskandar_soul < 0:
                self.iskandar_soul = 0
                print("Iskandar o'ldi")
                break
            print(f"Iskandarni joni: {self.iskandar_soul} qoldi")

        if self.polat_soul > 0:
            print("Polat yutdi")

        else:
            print("Iskandat yutdi")


ot = kurtlat_vodisi()
ot.otishmani_boshlash()
