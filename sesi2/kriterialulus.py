Eng = int(input("Masukkan nilai English: "))
MTK =  int(input("Masukkan nilai MTK: "))
Indo =  int(input("Masukkan nilai Indo: "))
Ipa = int(input("Masukkan nilai Ipa: "))
Ips = int(input("Masukkan nilai Ips: "))

rata1 = (MTK+Eng+Indo)/3
rata2 = (MTK+Eng+Indo+Ipa+Ips)/5

print(rata1, rata2)

if rata1>=75:
    print("Lulus")
elif rata2>=70:
    print("lulus")
elif (MTK and Eng)>=90:
    print("Lulus")
else:
    print("Tidak Lulus")
