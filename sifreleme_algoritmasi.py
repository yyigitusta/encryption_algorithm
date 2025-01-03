import numpy as np
import random

def harita_uret():
    # Kullanıcıdan sayı aralığını al
    print("Lütfen harita için sayı aralığını giriniz.")
    alt_sinir = int(input("Alt sınır: "))
    ust_sinir = int(input("Üst sınır: "))
    
    if alt_sinir >= ust_sinir:
        print("Geçerli bir aralık giriniz! Alt sınır üst sınırdan küçük olmalıdır.")
        return

    # Kullanıcıdan harita boyutunu al
    print("Lütfen harita boyutunu giriniz (örnek: 8x8).")
    boyut = int(input("Kare boyutunu al: "))
    
    # Belirtilen sayı aralığı ve boyuta göre harita oluştur
    harita = np.random.randint(alt_sinir, ust_sinir + 1, size=(boyut, boyut))
    
    # Rastgele başlangıç koordinatını seç
    x = random.randint(0, boyut - 1)
    y = random.randint(0, boyut -…
[18:02, 23.12.2024] +90 531 636 59 74: import numpy as np
import random

def harita_uret():
    # Kullanıcıdan sayı aralığını al
    print("Lütfen harita için sayı aralığını giriniz.")
    alt_sinir = int(input("Alt sınır: "))
    ust_sinir = int(input("Üst sınır: "))
    
    if alt_sinir >= ust_sinir:
        print("Geçerli bir aralık giriniz! Alt sınır üst sınırdan küçük olmalıdır.")
        return

    # Kullanıcıdan harita boyutunu al
    print("Lütfen harita boyutunu giriniz (örnek: 8x8).")
    boyut = int(input("Kare boyutunu al: "))
    
    # Belirtilen sayı aralığı ve boyuta göre harita oluştur
    harita = np.random.randint(alt_sinir, ust_sinir + 1, size=(boyut, boyut))
    
    # Rastgele başlangıç koordinatını seç
    x = random.randint(0, boyut - 1)
    y = random.randint(0, boyut -…
[18:19, 23.12.2024] +90 551 163 53 17: import numpy as np
import random

def harita_uret():
    # Kullanıcıdan sayı aralığını al
    print("Lütfen harita için sayı aralığını giriniz.")
    alt_sinir = int(input("Alt sınır: "))
    ust_sinir = int(input("Üst sınır: "))

    if alt_sinir >= ust_sinir:
        print("Geçerli bir aralık giriniz! Alt sınır üst sınırdan küçük olmalıdır.")
        return

    # Kullanıcıdan harita boyutlarını al
    print("Lütfen harita boyutlarını giriniz (örnek: 8x10).")
    satir = int(input("Satır sayısı: "))
    sutun = int(input("Sütun sayısı: "))

    # Belirtilen sayı aralığı ve boyutlara göre harita oluştur
    harita = np.random.randint(alt_sinir, ust_sinir + 1, size=(satir, sutun))

    # Rastgele başlangıç koordinatını seç
    x = random.randint(0, satir - 1…
[18:40, 23.12.2024] +90 531 636 59 74: import numpy as np
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
