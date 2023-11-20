def zamien_tab(T):
    n = len(T)
    for i in range(n):
        x = T[i]
        j = 2
        zamien = 1
        while x != 1:
            mno = 1
            while x % j == 0:
                x //= j
                mno = j
            zamien *= mno
            j += 1
        T[i] = zamien

def zgodne(T):
    n = len(T)
    cnt = 0
    for i in range(n):
        for j in range(i - 2, i + 3):
            if 0 <= j < n and i != j and T[i] == T[j]:
                cnt += 1
                break
    return cnt


T = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]
zamien_tab(T)
print(zgodne(T))
