N, M = input().split()  # numero aristas, numero vertices

n = int(N)
m = int(M)
g = []
matrix = [[0 for x in range(n)] for y in range(n)]

for j in range(n):
    g.append([])

for k in range(m):
    a1, a2, c = input().split()
    arista1 = int(a1)
    arista2 = int(a2)
    coste = int(c)
    g[arista1].append(arista2)
    matrix[arista1][arista2] = coste



def dfs(g, matrix):
    cont = 0
    maxdist = 0
    n = len(g)
    visited = [False] * n
    for v in range(n):
        cont = 0
        dfsRec(g, visited, v, matrix, cont)
        if cont > maxdist:
            maxdist = cont
    print(maxdist)


def dfsRec(g, visited, v, matrix, cont):
    visited[v] = True
    # print(v, end=" ")
    for adj in g[v]:
        if not visited[adj]:
            cont += matrix[v][adj]
            dfsRec(g, visited, adj, matrix, cont)


dfs(g, matrix)
