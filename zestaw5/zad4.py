def zad4(T):
    n = len(T)
    x = [-2,-1,1,2,2,1,-1,-2]
    y = [1,2,2,1,-1,-2,-2,-1]

    def mozliwe(w,k):
        if 0 <= w < n and 0 <= k < n:
            return True
        return False

    def rec(w=0,k=0,num=1):
        T[w][k] = num
        if num == n*n:
            return True
        for i in range(8):
            next_w = w + x[i]
            next_k = k + y[i]
            if mozliwe(next_w,next_k) and T[next_w][next_k] == 0:
                if rec(next_w,next_k,num+1):
                    return True
        T[w][k] = 0
        return False

    return rec()


l = 5
tab = [[0 for _ in range(l)] for _ in range(l)]
zad4(tab)
for row in tab:
    print(row)
