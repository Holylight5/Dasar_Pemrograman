#Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method. Input: [8, 3, 12, 4, 7, 2] Output: [12, 8, 7, 4, 0, 0]
Array_I = [8, 3, 12, 4, 7, 2]

for i in range (len(Array_I)):
    if Array_I[i] < 5:
        Array_I[i] = 0

Array_I.sort(reverse=True)

print(Array_I)