#Tuliskan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih besar, 2 bilangan lebih besar dari yang lain atau semua bilangan sama besar
a = int(input("Masukkan angka: "))
b = int(input("Masukkan angka: "))
c = int(input("Masukkan angka: "))

if a>b>c:
    print("Bilangan", a,"merupakan bilangan yang paling besar dari",b,"dan",c)
elif a==b and c<a:
        print("Bilangan a dan bilangan b memiliki nilai yang sama besar dan lebih besar dari nilai yang lain")
elif a<b>c:
      print("Bilang", b, "merupakan bilangan yang paling besar dari",a,"dan",c)
elif a==c and b<a:
      print("Bilangan a dan bilangan c memiliki nilai yang sama besar dan lebih besar dari nilai yang lain")
elif a<b<c:
      print("Bilang", c, "merupakan bilangan yang paling besar dari",a,"dan",b)
elif b==c and a<b:
      print("Bilangan b dan bilangan c memiliki nilai yang sama besar dan lebih besar dari nilai yang lain")
elif a==b==c:
      print("Semua bilangan memiliki nilai yang sama")
else:
      print("input salah")