# TODO Найдите количество книг, которое можно разместить на дискете
I = 1.44
kstr = 100
chstr = 50
ksim = 25
code = 4

I = I * 1024 * 1024
kniga = code * ksim * chstr * kstr
kolvo = I/kniga
print("Количество книг, помещающихся на дискету:", int(kolvo))
