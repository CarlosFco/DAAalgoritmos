from collections import deque

g = []
distance = []


n, m = input().split()
N = int(n)
M = int(m)

for i in range(N):
    distance.append([None] * N)
    g.append([])


for i in range(M):
    a1, a2, p = input().split()
    arista1 = int(a1)
    arista2 = int(a2)
    peso = int(p)
    distance[arista1][arista2] = peso * -1
    g[arista1].append(arista2)


def auxtopo(data, i):
    data["visited"][i] = True
    for next in data["graph"][i]:
        if not data["visited"][next]:
            auxtopo(data, next)
    data["toposort"].appendleft(i)

def toposort(g):
    data = {
        "graph": g,
        "toposort": deque(),
        "visited": [False] * N
    }
    for i in range(N):
        if not data["visited"][i]:
            auxtopo(data, i)
    return data["toposort"]


def dora(g):
    topolist = toposort(g)
    acumDistances = [0] * N
    for i in topolist:
        for next in g[i]:
            d = distance[i][next] + acumDistances[i]
            if d < acumDistances[next]:
                acumDistances[next] = d
    max = 0
    for i in acumDistances:
        i = i * -1
        if max < i:
            max = i
    print(max)

dora(g)



