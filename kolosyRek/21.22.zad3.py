def relatively_prime(x,y):
    if nwd(x,y) == 1:
        return True
    return False


def nwd(a,b):
    if b == 0:
        return a
    return nwd(b,a%b)


def l_tower(t, w=0, k=0, i=0, mov=0, last=""):
    if w == k == len(t)-1:
        return mov
    if i > len(t):
        return False
    if 0 <= i <= len(t) and i != k and relatively_prime(t[w][i], t[w][k]) and last == "w":
        return l_tower(t, w, i, 0, mov + 1, last="k")
    elif 0 <= i <= len(t) and i != w and relatively_prime(t[i][k], t[w][k]) and last == "k":
        return l_tower(t, i, k, 0, mov + 1, last="w")
    elif last == "":
        return l_tower(t,w,k,i,mov,"w") or l_tower(t,w,k,i,mov,"k")
    return l_tower(t,w,k,i+1,mov,last)


t = [[2,6,6,3,6,6],
     [6,6,6,6,6,6],
     [6,3,6,2,6,6],
     [6,6,6,6,6,6],
     [6,6,6,6,6,6],
     [6,2,6,6,6,3],
     ]

print(l_tower(t))
