t = input()
T = int(t) # casos a probar

sol = []

for i in range(T):
    n = input()
    N = int(n)  # numero de actividades
    timesaux = []
    timesaux.append(input().split())
    times = timesaux[0]
    activities = []
    cont = 0
    while cont < len(times):
        iniaux = times[cont]
        ini = int(iniaux)
        cont += 1
        finaux = times[cont]
        fin = int(finaux)
        cont += 1
        duration = fin - ini
        activities.append([duration, ini, fin])

    activities.sort()

    cont = 1
    previous = activities.pop(0)
    while activities:
        current = activities.pop(0)
        if previous[2] <= current[1]:
            cont += 1
            previous = current
    sol.append(cont)

for i in sol:
    print(i)