import random
import time
import os


def giris():
    print(">>> Oyuna Hoşgeldin")
    print(">>> Bilgisayar 0'dan 10'a kadar bir sayı tutacak ve sende tahmin etmeye çalışacaksın")
    time.sleep(1)
    print(">>> Oyun Başlıyor")
    print("-")
    time.sleep(0.5)
    print("--")
    time.sleep(0.5)
    print("---")
    print(">>> Bilgisayar 10'a kadar bir sayı tuttu aklından")
    return ">>> Hadi tahmin et o sayı'yı"


while True:
    print(giris())
    try:
        ins = int(input("-> "))
    except:
        print(">>> Hata Raporu Alındı!")
        print(".")
        print(".")
        time.sleep(0.5)
        print(">>> Oyun Baştan Başlatılıyor")
        time.sleep(1)
        os.system("cls")
        print(">>> Oyuna Hoşgeldin")
        print(">>> Bilgisayar 0'dan 10'a kadar bir sayı tutacak ve sende tahmin etmeye çalışacaksın")
        print()
        print(">>> Oyun Başlatılıyor")
        print("-")
        print("--")
        print("---")
        print(">>> Bilgisayar 10'a kadar bir sayı tuttu aklından")
        print(">>> Hadi tahmin et o sayı'yı")
        os.system("cls")
    else:
        print(">>> Kontrol ediliyor")
        print("-")
        time.sleep(0.5)
        print("--")
        time.sleep(0.5)
        print("---")
        pctutugu = random.randint(0, 10)
        if ins == pctutugu:
            print(">>> Cevabı Doğru Bildin Tebrikler")
            pctutugu = print(">>>", pctutugu, "Bilgisayarın Tutuğu sayı")
            input(">>> Devam etmek için herhangi bir tuşa bas... ")
        elif ins != pctutugu:
            print(">>> Cevabı doğru bilemedin malesef!")
            pctutugu = print(">>>", pctutugu, "Bilgisayarın Tutuğu sayı")
            input(">>> Devam etmek için herhangi bir tuşa bas... ")
            print(">>> Oyun baştan başlatılıyor")
            print("-")
            time.sleep(0.5)
            print("--")
            time.sleep(0.5)
            print("---")
            os.system("cls")
