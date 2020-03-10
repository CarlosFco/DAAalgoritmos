#   still don't know wtf i need to do

n, m, t = input().split()
N = int(n)  # numero de nodos
M = int(m)  # numero de vertices
T = int(t)  # peso maximo

graph = []
for i in range(N):
    graph.append([])

for i in range(M):
    h1, h2, d = input().split()
    H1 = int(h1)    # node 1
    H2 = int(h2)    # node 2
    D = int(d)      # weight
    graph[H1].append([H1, H2, D])
    graph[H2].append([H2, H1, D])


# Complexity O(V)
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
    initial = 0
    visit = [False] * len(graph)
    mst = 0

    visit[initial] = True
    shortest_edges = [float('inf')] * len(graph)
    for start, end, weight in graph[initial]:
        shortest_edges[end] = weight

    for i in range(1, len(graph)):
        next_node, cost = __select_min__(shortest_edges, visit)
        if cost < float('inf'):  # if not unreachable
            visit[next_node] = True
            mst += cost
            for edge in graph[next_node]:
                start, end, weight = edge
                if not visit[end]:
                    shortest_edges[end] = min(shortest_edges[end], weight)

    return mst


minweight = prim(graph)
nodespassed = len(graph) - 1
minweight += nodespassed
if(minweight <= T):
    print(minweight)
else:
    print("Somos un fraude")