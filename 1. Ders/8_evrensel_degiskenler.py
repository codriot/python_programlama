a = 5


def b():
    a = 10
    print(a)


b()
print(a)


def c():
    global a  # bu ifade a değişkenini tüm sayfada düzenler
    a = 10
    print(a)


c()
print(a)
