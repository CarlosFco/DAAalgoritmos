# timepo espera y mochila es optimo
import sys
from random import random


def getBestTask(candidates, tasks):
    besttimetask = sys.maxsize
    besttask = 0
    for c in candidates:
        time = tasks[c]
        if time < bestTimeTask:
            bestTimeTask = time
            bestTask = c
    return bestTask


def greedyWaitingTime(tasks):
    candidates = set()  # conjunto vacio
    n = len(tasks)
    for i in range(n):
        candidates.add(i)
    sol = []
    while candidates: # si tiene algo es true
        bestTask = getBestTask(candidates, tasks)
        candidates.remove(bestTask);
        sol.append(bestTask)
    return sol


n = 10
tasks = []
for i in range(n):  # de 0 a 9
    tasks.append(random.uniform(44, 140))
sol = greedyWaitingTime(tasks)
