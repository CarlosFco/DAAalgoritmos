n, m = input().split()
N = int(n)  # numero de nodos
M = int(m)  # numero de aristas

graph = []
for i in range(N + 1):
    graph.append([])

for i in range(M):
    s, e, w = input().split()
    start = int(s)
    end = int(e)
    weight = int(w)
    graph[start].append([start, end, weight])
    graph[end].append([end, start, weight])


def __select_min__(shortest_edges, visit):
    vertex = None
    weight = float('inf')
    for i in range(1, len(shortest_edges)):
        if not visit[i] and shortest_edges[i] < weight:
            vertex = i
            weight = shortest_edges[i]
    return vertex, weight


# Complexity: O(V*E)
def prim(graph):
    # graph nodes go from 1 to N
    initial = 1
    visit = [False] * len(graph)
    mst = 0

    visit[initial] = True
    shortest_edges = [float('inf')] * len(graph)
    for start, end, weight in graph[initial]:
        shortest_edges[end] = weight

    for i in range(2, len(graph)):
        next_node, cost = __select_min__(shortest_edges, visit)
        if cost < float('inf'):  # if not unreachable
            visit[next_node] = True
            mst += cost
            for edge in graph[next_node]:
                start, end, weight = edge
                if not visit[end]:
                    shortest_edges[end] = min(shortest_edges[end], weight)

    return mst

print(prim(graph))