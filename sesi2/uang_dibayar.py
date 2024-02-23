beli_kilo = int(input("Masukkan kilo: "))

if beli_kilo <=2:
    harga = beli_kilo*20000
elif beli_kilo <=5:
    harga = beli_kilo*18000
else:
    harga= beli_kilo*16000
print("Harga yang harus dibayar untuk", beli_kilo," mangga adalah", harga)

print("="*30)
#Panggilan berdasarkan umur
umur= int(input("Masukkan umur: "))

if umur<=2:
    print("Bayi")
elif umur <=5:
    print("Balita")
elif umur <=12:
    print("Anak-anak")
elif umur <=17:
    print("Remaja")
elif umur <30:
    print("Dewasa")
else :
    print("Tua")

