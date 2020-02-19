from collections import deque


def topsort(g):
    data = {
        "g": g,
        "state": dict(),
        "parent": dict(),
        "d": dict(),
        "time": 0,
        "f": dict(),
        "list": deque()
    }
    for k in g.keys():
        data["state"][k] = "NOT_VISITED"
        data["parent"][k] = None
        data["d"][k] = 0
        data["f"][k] = 0
