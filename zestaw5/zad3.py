def zad3(T, x):
    n = len(T)
    min_sum = 10**10

    def krol(w, k, suma):
        nonlocal min_sum, n
        if w == n:
            min_sum = min(min_sum, suma)
            return
        suma += T[w][k]
        if k > 0:
            krol(w+1,k-1, suma)
        krol(w+1,k,suma)
        if k < n-1:
            krol(w+1,k+1,suma)

    krol(0,x,0)
    return min_sum


tab = [
    [5,3,7,5,3],
    [6,5,3,8,9],
    [5,9,3,6,8],
    [7,9,2,5,1],
    [6,8,1,3,6]
]
print(zad3(tab,4))

