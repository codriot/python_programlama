a = 10
print(type(a))
a = float(10)
print(type(a))
a = str(10)
print(type(a))


class a:
    sinifinIcindekiSayisi = 10  # sınıflar type olarak geçiyor


kopyaclass = a
print(type(a))
print(type(kopyaclass))
print(kopyaclass.sinifinIcindekiSayisi)
print(type(kopyaclass.sinifinIcindekiSayisi))
