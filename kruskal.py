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


def updateComponents(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(g):
    components = list(range(len(g)))
    cont = len(g) - 1
    mst = 0
    list_edges = []
    for adj in g:
        for start, end, weight in adj:
            if start < end:
                list_edges.append([weight, start, end]) # sort ordena en base al primer elemento de la tupla
    list_edges.sort()
    i = 0
    while len(list_edges) > i and cont > 1:
        if components[start] != components[end]:
            mst = weight
            cont -= 1
            updateComponents(components, components[start], components[end])
        i += 1
    return mst


print(kruskal(graph))
