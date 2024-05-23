#Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method.
#Input: [8, 3, 12, 4, 7, 2]
#Output: [12, 8, 7, 0, 0, 0]

List = [8, 3, 12, 4, 7, 2]

for i in range (len(List)):
    if List[i] < 5:
        List[i] = 0

List.sort(reverse=True)
print(List)