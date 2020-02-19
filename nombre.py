n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
# print(list)

m = int(input())
list2 = []
for i in range(m):
    list2.append(input())
# print(list2)

cont = 0
for i in list2:
    for j in list1:
        if i == j:
            cont = cont + 1
    if cont == 0:
        print("NUEVO")
    else:
        print(cont)
    cont = 0
