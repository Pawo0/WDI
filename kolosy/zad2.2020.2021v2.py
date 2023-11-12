def wieksza_od_max(maks,t):
    n = len(maks)
    for i in range(n):
        if maks[i] > t[i]:
            return False
        elif maks[i] < t[i]:
            return True


def mniejsza_od_max(maks,t):
    n = len(maks)
    for i in range(n):
        if maks[i] > t[i]:
            return True
        elif maks[i] < t[i]:
            return False


def distance(T):
    n = len(T)
    maks = [0] * n
    maks_i = 0
    mini = [0] * n
    mini_i = 0
    for i in range(n):
        wiersz = T[i]
        if wieksza_od_max(maks, wiersz):
            maks = wiersz
            maks_i = i
        if mniejsza_od_max(mini, wiersz):
            mini = wiersz
            mini_i = i
    return abs(mini_i-maks_i)


t = [[0,0,1,0],
     [1,0,0,1],
     [1,1,0,0],
     [0,1,1,0],
     [0,0,1,1]
     ]

print(distance(t))