n = input()
N = int(n) # piezas disponibles a elegir

m = input()
M = int(m) # peso maximo

type = input()

maxweight = 0

if type == "ligero":
    maxweight = M * 0.5
elif type == "medio":
    maxweight = M * 0.75
elif type == "pesado":
    maxweight = M


pieces = []

for i in range(N):
    cloth, w, v = input().split()
    weight = int(w)
    value = int(v)
    profit = value / weight
    pieces.append([profit, cloth, weight, value])


pieces.sort(reverse = True)

currentweight = 0
issol = False
cont = 0
sol = []
defense = 0

# print(pieces)
# print(pieces[cont][2])

while not issol and cont < len(pieces):
    if (pieces[cont][2] + currentweight) <= maxweight:
        sol.append(pieces[cont][1])
        currentweight += pieces[cont][2]
        defense += pieces[cont][3]
        cont += 1
    else:
        free = maxweight - currentweight
        assigned = free /pieces[cont][2]
        defeseaquired = pieces[cont][3] * assigned
        defense += defeseaquired
        sol.append(pieces[cont][1])
        issol = True


print('{:.2f}'.format(round(defense, 2)))
sol.sort()
for i in sol:
    print(i)


