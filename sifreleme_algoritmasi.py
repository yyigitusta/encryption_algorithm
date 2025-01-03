import numpy as np
import random

def harita_uret():
    

    print("Lütfen harita için sayı aralığını giriniz.")
    alt_sinir = int(input("Alt sınır: "))
    ust_sinir = int(input("Üst sınır: "))

    if alt_sinir >= ust_sinir:
        print("yanlış secim")
        return

    # harita boyutları gir
    print("Lütfen harita boyutlarını giriniz (örnek: 8x10).")
    satir = int(input("Satır sayısı: "))
    sutun = int(input("Sütun sayısı: "))

    # random harita oluşturma matrixe dönüştürme
    harita = np.random.randint(alt_sinir, ust_sinir + 1, size=(satir, sutun))

    # başlangıç koordinatını 
    x = random.randint(0, satir - 1)
    y = random.randint(0, sutun - 1)

    
    print("\nOluşturulan Harita:")
    print(harita)
    print(f"\nRastgele Başlangıç Koordinatları: (x, y) = ({x}, {y})")

    # hangi yol 
    secim = random.randint(1, 3)
    print(f"\nSeçilen Yol: {secim}")

    # XOR işlemi için başlangıç
    sonuc = 0   # etkisiz eleman
 
    
    if secim == 1:
        print("secilen yol 1")
        hareketler = [(x, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1)]

    elif secim == 2:
        print("secilen yol 2")
        hareketler = [(x, y), (x, y + 1), (x + 1, y + 1), (x + 1, y + 2)]

    elif secim == 3:
        print("secilen yol 3")
        hareketler = [(x, y), (x, y + 1), (x + 1, y + 1), (x + 1, y + 3), (x, y + 3)]

    # taşma kontrolu yapılarak hareketleri ayarla
    for (satir_hareket, sutun_hareket) in hareketler:
        satir_hareket = satir_hareket % satir
        sutun_hareket = sutun_hareket % sutun  

        print(f"XOR {sonuc} ^ {harita[satir_hareket][sutun_hareket]} = {sonuc ^ harita[satir_hareket][sutun_hareket]}")
        sonuc ^= harita[satir_hareket][sutun_hareket]

    #  kullanıcıdan alınan sayı ile xor laam işlemi
    kullanici_sayisi = int(input("\nBir sayı giriniz: "))
    print(f"Sonuç XOR {sonuc} ^ {kullanici_sayisi} = {sonuc ^ kullanici_sayisi}")
    sonuc ^= kullanici_sayisi

    # Nihai sonuç
    print(f"\nSonuç: {sonuc}")

# Fonksiyonu çağır
harita_uret()
