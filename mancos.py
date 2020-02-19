list = []
suma = 0;

n = int(input())

for i in range(n):
    a = int(input())
    list.append(a)
    suma = suma + a

media = suma // n

for i in list:
    if i > media:
        print(i)