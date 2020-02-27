from random import randint

graph = [
    [],
    [(1, 3, 1), (1, 4, 2), (1, 7, 6)],
    [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
    [(3, 1, 1), (3, 7, 5), (3, 4, 3)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)]
]


def selectMin(shortest_edges, visited):
    vertex = None
    weight = float('inf')
    for i in range(1, len(shortest_edges)):
        if not visited[i] and shortest_edges[i] < weight:
            vertex = i
            weight = shortest_edges[i]
    return vertex, weight


def prim(graph):
    initial = randint(1, len(graph))
    visited = [False] * len(graph)
    mst = 0
    visited[initial] = True
    shortest_edges = [float('inf')] * len(graph)
    for start, end, weight in graph[initial]:
        shortest_edges[end] = weight
    for i in range(2, len(graph)):
        next_node, cost = selectMin(shortest_edges, visited)
        if cost < float('inf'):
            visited[next_node] = True
            mst += cost
            for edge in graph(next_node):
                start, end, weight = edge
                shortest_edges[end] = min(shortest_edges[end], weight)

prim(graph)