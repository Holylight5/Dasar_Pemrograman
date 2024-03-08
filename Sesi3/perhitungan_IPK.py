def konversi_nilai(nilai_matkul):
    if nilai_matkul >= 80:
        return "A"
    elif nilai_matkul >= 65:
        return "B"
    elif nilai_matkul >= 50:
        return "C"
    elif nilai_matkul >= 35:
        return "D"
    else:
        return "E"
    

Algoritma = float(input("Masukkan nilai: "))
Perancangan_Objek = float(input("Masukkan nilai: "))
Kalkulus = float(input("Masukkan nilai: "))
Etika_Profesi = float(input("Masukkan nilai: "))
Database =float(input("Masukkan nilai: "))
English =float(input("Masukkan nilai: "))

def konversi_bobot(nilai_huruf):
    bobot = {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 1,
        'E': 0
    }
    return bobot.get(nilai_huruf, 0)

nilai_huruf1 = konversi_nilai(Algoritma)
nilai_huruf2 = konversi_nilai(Perancangan_Objek)
nilai_huruf3 = konversi_nilai(Kalkulus)
nilai_huruf4 = konversi_nilai(Etika_Profesi)
nilai_huruf5 = konversi_nilai(Database)
nilai_huruf6 = konversi_nilai(English)

#SKS
sksAlgoritma= 3
sksPO= 3
skskalkulus= 3
sksEtika= 3
sksDatabase= 3
sksEnglish= 3

total_sks = sksPO + skskalkulus + sksDatabase + sksAlgoritma + sksEnglish + sksEtika

#Nilai
total_nilai_Algoritma = sksAlgoritma*konversi_bobot(nilai_huruf1)
total_nilai_PO = sksPO*konversi_bobot(nilai_huruf2)
total_nilai_kalkulus = skskalkulus*konversi_bobot(nilai_huruf3)
total_nilai_Etika = sksEtika*konversi_bobot(nilai_huruf4)
total_nilai_Database = sksDatabase*konversi_bobot(nilai_huruf5)
total_nilai_English = sksEnglish*konversi_bobot(nilai_huruf6)

total_semua = total_nilai_Database + total_nilai_Etika + total_nilai_Algoritma + total_nilai_English + total_nilai_English + total_nilai_PO
#IPK
IPK = total_semua / total_sks




print("Nilai Algoritma:", konversi_nilai(Algoritma))
print("Bobot untuk nilai PAlgoritma:", konversi_bobot(konversi_nilai(Algoritma)))
print("Total nilai algoritma: ", total_nilai_Algoritma)
print("Nilai Perancangan objek:", konversi_nilai(Perancangan_Objek))
print("Bobot untuk nilai Perancangan Objek:", konversi_bobot(konversi_nilai(Perancangan_Objek)))
print("Total nilai Perancangan Objek: ",total_nilai_PO)
print("Nilai Kalkulus:", konversi_nilai(Kalkulus))
print("Bobot untuk nilai Kalkulus:", konversi_bobot(konversi_nilai(Kalkulus)))
print("Total nilai Kalkulus: ",total_nilai_kalkulus)
print("Nilai Etika profesi:", konversi_nilai(Etika_Profesi))
print("Bobot untuk nilai Etika Profesi:", konversi_bobot(konversi_nilai(Etika_Profesi)))
print("Total nilai Etika: ",total_nilai_Etika)
print("Nilai Database:", konversi_nilai(Database))
print("Bobot untuk nilai Database:", konversi_bobot(konversi_nilai(Database)))
print("Total nilai Database: ", total_nilai_Database)
print("Nilai English:", konversi_nilai(English))
print("Bobot untuk nilai English:", konversi_bobot(konversi_nilai(English)))
print("Total nilai ENlish: ", total_nilai_English)

print("Jumlah SKS: ",total_sks)
print("Total Semua nilai: ",total_semua)
print("IPK yang didapatkan: ",IPK)


