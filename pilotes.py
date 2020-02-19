from collections import deque

N, M = input().split() # numero de aristas, numero de vertices
g = []
m = int(M)

n = int(N)
for i in range(n):
    g.append([])

m = int(M)
for i in range(m):
    a1, a2 = input().split()
    arista1 = int(a1)
    arista2 = int(a2)
    g[arista1].append(arista2)
    g[arista2].append(arista1)


def bfs(g):
    cont = 0
    n = len(g)
    visited = [False] * n
    for v in range(1, n):
        if not visited[v]:
            bfsAux(g, visited, v, cont)
            cont += 1
    print(cont)


def bfsAux(g, visited, v, cont):
    q = deque()
    visited[v] = True
    #print(v, end=" ")
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                #print(adj, end=" ")
                q.append(adj)


bfs(g)