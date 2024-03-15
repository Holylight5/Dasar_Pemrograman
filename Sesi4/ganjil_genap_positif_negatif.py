#Tuliskan program untuk menentukan bilangan itu bilangan (ganjil/genap) positif, negatif atau 0
a = int(input("Masukkan angka: "))

if a%2==0:
    if a>0:
        print("Bilang", a, "merupakan bilangan genap positif")
    elif a<0:
        print("Bilang", a, "merupakan bilangan genap negatif")
    else:
        print("Bilangan", a, "adalah bilangan nol")

else:
    if a>0:
        print("Bilang", a, "merupakan bilangan ganjil positif")
    elif a<0:
        print("Bilang", a, "merupakan bilangan ganjil negatif")

