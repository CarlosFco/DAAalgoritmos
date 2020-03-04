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

