Array_I = [7, 4, 9, 2, 5, 1]

for i in Array_I[:]:
    if i % 2 != 0:
        Array_I.remove(i)

Array_I.sort()

print(Array_I)