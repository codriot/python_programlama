sayi_listesi = [3, 5, 10, -8, 9, 15]
a = sayi_listesi
print(a)

sayi_listesi.sort()
print(a)  # oto güncelliyor, yüksek ihtimalle referansını alıyor yeniden tanımlamıyor

##############################
sayi_listesi = [3, 5, 10, -8, 9, 15]
a = sayi_listesi.copy()
print(a)

sayi_listesi.sort()
print(a)  # copy yapınca yeni tanımlıyor galiba
