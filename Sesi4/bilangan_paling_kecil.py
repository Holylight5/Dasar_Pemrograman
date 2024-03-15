#Tulisan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih kecil
a = int(input("Masukkan angka: "))
b = int(input("Masukkan angka: "))
c = int(input("Masukkan angka: "))

if a<b<c:
    print("Bilangan", a, "Merupakan bilangan yang paling kecil diantara", b, "dan", c)
elif a>b<c:
    print("Bilangan", b, "Merupakan bilangan yang paling kecil diantara", c, "dan", a)
else:
    print("Bilangan", c, "Merupakan bilangan yang paling kecil diantara", a, "dan", b)
    if b==a and c<a:
        print("Bilangan", c, "Merupakan bilangan yang paling kecil diantara", a, "dan", b)
