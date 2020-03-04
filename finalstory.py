t = input()
T = int(t) # numero de combates

data = {
    "enemiesatks" : [],
    "enemiesps" : [],
    "playeratk" : [],
    "profit" : []
}

pos = 0

for i in range(T):
    a = input()
    myatk = int(a) # ataque del jugador en este combate
    data["playeratk"].append(myatk)
    en = input()
    nenemies = int(en) # numero de enemigos
    atkslist = []
    atkslist.append(input().split()) #ataques de los enemigos
    pslist = []
    pslist.append(input().split()) #vidas de los enemigos
    auxatks = atkslist[0]
    auxps = pslist[0]
    divs = []
    for j in range(len(auxatks)):
        auxatks[j] = int(auxatks[j])
        auxps[j] = int(auxps[j])
        divs.append(auxatks[j] / auxps[j])
    data["enemiesatks"].append(auxatks)
    data["enemiesps"].append(auxps)
    data["profit"].append(divs)

# print(data)

# ya esta tod guardado

def getmaxprofit(profit):
    cont = 0
    max = 0
    for i in range(len(profit)):
        if profit[i] >= max:
            max = profit[i]
            cont = i
    return cont

def isdone(ps):
    for i in ps:
        if i != 0:
            return False
    return True


def greedy(data):
    for i in range(T):
        dmgreceievd = 0
        currenttarget = getmaxprofit(data["profit"][i])
        data["profit"][i][currenttarget] = 0
        # comienza la batalla
        done = False
        while not done:
            cont = 0
            for j in data["enemiesatks"][i]:
                if data["enemiesps"][i][cont] > 0:
                    dmgreceievd += j
                cont += 1
            data["enemiesps"][i][currenttarget] -= data["playeratk"][i]
            if data["enemiesps"][i][currenttarget] <= 0:
                data["profit"][i][currenttarget] = 0
                currenttarget = getmaxprofit(data["profit"][i])
                if data["enemiesps"][i][currenttarget] <= 0:
                    done = True
        print(dmgreceievd)


greedy(data)

