t, o, p = input().split()
T = int(t)  # posicion inicial
O = int(o)  # posicion del objetivo (final)
P = int(p)  # potencia del disparo

n, m = input().split()
N = int(n)  # numero nodos
M = int(m)  # numero aristas

costaux = []
costaux.append(input().split())
costaux = costaux[0]
cost = []   # coste del rebote en cada nodo
for i in costaux:
    cost.append(int(i))

graph = []
for i in range(N + 1):  # para ajustar que empieza en 1
    graph.append([])

for i in range(M):
    s, e = input().split()
    start = int(s)
    end = int(e)
    graph[start].append([start, end, cost[end - 1]])
    graph[end].append([end, start, cost[start - 1]])


def selectMin(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index


def dijkstra(origin, destination, graph):
    distances = [float('inf')] * len(graph)
    visited = [False] * len(graph)
    distances[origin] = 0   # la distancia a uno mismo
    visited[origin] = True
    for start, end, weight in graph[origin]:
        distances[end] = weight
    for i in range(2, len(graph)):  # 2 porque la primera distancia ya esta calculada (y empieza desde el nodo 1)
        nextNode = selectMin(distances, visited)    # selecciona nodo mas cercano que no haya sido visitado
        visited[nextNode] = True
        for start, end, weight in graph[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight) # distances[end] es desde el nuevo origen hasta el siguiente
                                                                            # distances[start] + weight es la ditancia desde el nuevo origen hasta el anterior mas el peso de ir hasta el nuevo fin

    return distances[destination]

totalcost = dijkstra(T, O, graph)

totalcost -= cost[O - 1]

sol = P - totalcost

if sol <= 0:
    print(0)
else:
    print(sol)