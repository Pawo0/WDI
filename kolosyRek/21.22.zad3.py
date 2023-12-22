def relatively_prime(x,y):
    if nwd(x,y) == 1:
        return True
    return False


def nwd(a,b):
    if b == 0:
        return a
    return nwd(b,a%b)


def l_tower(t,w=0,k=0,mv=0):
    n = len(t)
    if w == k == n-1:
        return mv
    for i in range(k+1,n):
        if relatively_prime(t[w][k],t[w][i]):
            return l_tower(t,w,i,mv+1)
    for i in range(w+1,n):
        if relatively_prime(t[w][k], t[i][k]):
            return l_tower(t,i,k,mv+1)
    return -1


def r_tower(t,w,k,mv=0):
    n = len(t)
    if w == n-1 and k == 0:
        return mv
    for i in range(k -1, -1,-1):
        if relatively_prime(t[w][k], t[w][i]):
            return r_tower(t, w, i, mv + 1)
    for i in range(w +1, n):
        if relatively_prime(t[w][k], t[i][k]):
            return r_tower(t, i, k, mv + 1)
    return float('inf')

def race(t):
    n = len(t)
    speed_r1 = l_tower(t,0,0)
    speed_r2 = r_tower(t,0,n-1)
    if speed_r1 < speed_r2:
        return 1
    elif speed_r1 > speed_r2:
        return 2
    else:
        return 0


t = [[2,6,6,3,6,3],
     [6,6,6,6,6,6],
     [6,3,6,2,3,6],
     [6,6,6,6,6,6],
     [6,6,6,6,6,6],
     [3,2,6,6,2,3],
     ]

print(race(t))