liste = ["Elma", "Armut", "Ayva"]

liste.sort()  # başharfe göre sıralar
print(liste)

liste.reverse()  # listeyi ters çeviri
print(liste)


def fonksiyon(n):
    return abs(n - 30)  # mutlak değer


sayi_listesi = [100, -50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon)  # çalışmıyor bu nedense sor

print(sayi_listesi)


# doğrusu

def mutlak_deger_30_eksi(n):
    return abs(n - 30)


# Fonksiyonu test etmek için bir liste oluşturabiliriz.
sayi_listesi = [100, -50, 65, 82, 23]

# Liste elemanlarını işlemek için bir döngü kullanabiliriz.
sonuclar = [mutlak_deger_30_eksi(sayi) for sayi in sayi_listesi]
sonuclar.sort()
# Sonuçları yazdırabiliriz.
print(sonuclar)
