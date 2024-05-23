# Dewi memiliki dua list yang berisi nama-nama buah-buahan. Dia ingin menggabungkan kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama. Setelah itu, dia ingin mengurutkan sisa buah-buahan secara alfabetis. Bantu Dewi
# Input: ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]

listHasil = list1 + list2
listNotDuplicate = list(set(listHasil))
listNotDuplicate.sort()
print(listNotDuplicate)
