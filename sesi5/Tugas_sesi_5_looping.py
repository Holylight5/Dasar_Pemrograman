#No1
print(20*'=',"No 1",20*'=')
a=1
for i in range(3):
    print(a, ". aku cinta Indonesia", end=' ')
    a +=2
    print('\t')

#No2 
print(20*'=',"No 2",20*'=')
a=2
b=2
for i in range(6):
    print(a, end=' ')
    a +=b
    b +=1

#No3
print('\t')
print(20*'=',"No 3",20*'=')
a=1
b=1
c = a*b
for i in range(3):
    print(b,'x',a,'=',c, end=' ')
    a +=b
    c = a*b
    print('\t')

#No4
print(20*'=',"No 4",20*'=')
a=7
b=6
c=a*b
for i in range(5):
    print(a,'x',b,'=',c, end=' ')
    b +=1
    c=a*b
    print('\t')

#No5
print(20*'=',"No 5",20*'=')
for i in range(3):
    i = "*"
    print(".",i,i,i)

#No6
print(20*'=',"No 6",20*'=')
for i in range(3):
    i += 1
    print(i,i,i,i)

#No7
print(20*'=',"No 7",20*'=')
a = 0    
b = 1    
for i in range(10):  
    print(b, end = " ")  
    c = a+b                        
    a = b               
    b = c  
print('\t')

#No8
print(20*'=',"No 8",20*'=')  
a = 0
b = 1
c = 2
d = a + b + c
for i in range(10):
    print(b, end=' ')
    d = a + b + c
    a = b
    b = c
    c = d
print('\t')

#No9
print(20*'=',"No 9",20*'=')  
for i in range(4, 0, -1):
    print('1 '*i)

#No10
print(20*'=',"No 10",20*'=')  
list = [2,3,2,3,2]

for i in range(5):
    for j in range(i, 5):
        print(list[j], end=' ')
    print()
