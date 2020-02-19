import sys
from random import random


def getBestTask(candidates, tasks):
    besttimetask = sys.maxsize
    besttask = 0
    for c in candidates:
        time = tasks[c]
        if time < besttimetask:
            besttimetask = time
            besttask = c
    return besttask


def greedywaintgtime(tasks):
    candidates = set()
    n = len(tasks)
    for i in range(n):
        candidates.add(i)
    sol = []
    while candidates:
        besttask = getBestTask(candidates, tasks)
        candidates.remove(besttask)
        sol.append(besttask)
    return sol


n = 10
tasks = []
for i in range(n):
    tasks.append(random.uniform(44, 140))
sol = greedywaintgtime(tasks)
