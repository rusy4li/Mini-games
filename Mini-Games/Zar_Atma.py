from random import randint as r
import time
import os


def roll_dice():
    return r(1, 6)


os.system("cls")
print(">>> Oyuna Hoşgeldin")
print(">>> Kaç Kişi ile oynamak istiyorsunuz? [1],[2]")
while True:
    kackisi = input("->> ")

    if kackisi == "1":
        print(">>> İlk sen Başlıyorsun 'zar' yaz ve oyunu başlat")
        while True:
            zar = input("->> ")
            print(">>>", roll_dice())
            print("-")
            print(">>> Sıra bende")
            time.sleep(1)
            print(">>>", roll_dice())
            print("-")
            time.sleep(0.5)
            print(">>> sıra sende 'zar' yazmayı unutma!")
    elif kackisi == "2":
        print(">>> İki takım oluşturacaksınız")
        print(">>> İlk takımın İsmi?")
        isim1 = input("->> ")
        print(">>> İkinci takımın İsmi?")
        isim2 = input("->> ")
        print(">>> {} adlı takım başlıyor ilk".format(isim1))
        print(">>> 'zar' yazarak zar atacaksınız!")
        print(">>> Başla!!!")
        while True:
            zar = input("->> ")
            print(">>>", roll_dice())
            print("-")
            print(">>> Şimdi {} adlı takım zar atıcak".format(isim2))
            zar = input("->> ")
            print(">>>", roll_dice())
            print(">>> Şimdi tekrardan {} adlı takım zar atıyor".format(isim1))
    else:
        print(">>> Hata Raporu Alındı!")
        print(".")
        print(".")
        time.sleep(0.5)
        print(">>> Oyun Baştan Başlatılıyor")
        time.sleep(1)
        print()
        print(">>> Oyuna Hoşgeldin")
        print(">>> Kaç Kişi ile oynamak istiyorsunuz? [1],[2]")
