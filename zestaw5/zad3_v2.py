from math import inf

def zad3(t):
    n = len(t)
    def rec(w,k):
        if w == n:
            return 0
        if k < 0 or k >= n:
            return inf
        return min(rec(w+1,k-1),rec(w+1,k),rec(w+1,k+1)) + t[w][k]

    return rec(0,4)


tab = [
    [5,3,7,5,3],
    [6,5,3,8,9],
    [5,9,3,6,8],
    [7,9,2,5,1],
    [6,8,1,3,6]
]

print(zad3(tab))
