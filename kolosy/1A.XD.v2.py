def zgodne(T):
    n = len(T)
    tab = [0 for _ in range(n)]
    for i in range(n):
        if tab[i] == 0:
            rozk = rozklad(T[i])
            for j in range(i-2,i+3):
                if 0 <= j < n and i != j and rozk == rozklad(T[j]):
                    tab[i] = 1
                    tab[j] = 1
    return sum(tab)

def rozklad(x):
    set1 = set()
    j = 2
    while x != 1:
        while x % j == 0:
            x //= j
            set1.add(j)
        j += 1
    return set1



T = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]
print(zgodne(T))

