Array_I = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]

for i in Array_I[:]:
    if len(i) < 5:
        Array_I.remove(i)

Array_I.sort()

print(Array_I)