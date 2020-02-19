# optimo

n = 5
data = {}
data['profit'] = [20, 30, 66, 40, 60]
data['weight'] = [10, 20, 30, 40, 50]
data['maxweight'] = 100


def getBestItem(data, candidates):
    bestRatio = 0
    bestItem = 0
    for c in candidates:
        r = data['profit'][c] / data['weight'][c]
        if r > bestRatio:
            bestRatio = r
            bestItem = c
    return bestItem


def isFeasible(data, bestItem, freeweight):
    return data['weight'][bestItem] <= freeweight


def greedyknapsack(data):
    n = len(data['profit'])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    freeweight = data['maxweight']
    sol = [0] * n
    isSol = False
    while candidates and not isSol:
        bestItem = getBestItem(data, candidates)
        candidates.remove(bestItem)
        if isFeasible(data, bestItem, freeweight):
            sol[bestItem] = 1.0
            freeweight -= data['weight'][bestItem]
        else:
            sol[bestItem] = freeweight / data['weight'][bestItem]
            isSol = True
    return sol




sol = greedyknapsack(data)
print(sol)


