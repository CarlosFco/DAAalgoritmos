from collections import deque

N, M = input().split()  # numero aristas, numero vertices

n = int(N)
m = int(M)
coste = []
g = []

for i in range(n):
    c = input()
    c1 = int(c)
    coste.append(c1)

for j in range(n):
    g.append([])

for k in range(m):
    a1, a2 = input().split()
    arista1 = int(a1)
    arista2 = int(a2)
    g[arista1].append(arista2)
    g[arista2].append(arista1)

# print(coste)
# print(g)

done = [False] * n
costetotal = 0
visited = [False] * n


def bfsAux(g, visited, v):
    cont = 0
    q = deque()
    visited[v] = True
    # print(v, end=" ")
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                # print(adj, end=" ")
                q.append(adj)
                cont += 1
    for i in range(len(visited)):
        visited[i] = False
    return cont


for l in range(len(g)):
    if bfsAux(g, visited, l) == len(g):
        costetotal += coste[l]

# for l in range(len(g)):
#   cont = 0
#  for p in g:
#      cont += p.count(l)
# if (g[l] != []) and (len(g[l]) == 2) and (not done[l]) and (cont == 2):
#    done[l] = True
#   costetotal += coste[l]


print(costetotal)
