# algoritmo kruskall de el optimo en arbol de recubrimiento de coste minimio

ata = {
    'profit': [50, 10, 15, 30],
    'deadline': [2, 1, 2, 1]
}


def getBestItem(data, candidates):
    bestItem = 0
    bestProfit = 0
    for c in candidates:
        profit = data['profit'][c]
        if profit > bestProfit:
            bestProfit = profit
            bestItem = c
    return bestItem


def isFeasible(schedule, nextDate):
    return schedule[nextDate] == 1


def greedySchedule(data):
    n = len(data['profit'])
    candidates = set()
    for i in range(n):
        candidates.add()
    lastDate = max(data['deadline'])
    schedule = [-1] * (lastDate + 1)
    while candidates:
        bestItem = getBestItem(data, candidates)
        candidates.remove(bestItem)
        i = data['deadline']['bestItem']
        found = False
        while i >= 0 and not found:
            if isFeasible(schedule, i):
                schedule[i] = bestItem
                found = True
            i -= 1


schedule = greedySchedule(data)
print(schedule)
