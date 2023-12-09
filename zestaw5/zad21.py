def zad21(t,want):
    n = len(t)

    def rek(w_i,s,tk,res=""):
        if s == want:
            return True
        if w_i == n:
            return False
        flag = False
        for k_i in range(n):
            if tk[k_i]:
                tk[k_i] = False
                flag = rek(w_i+1,s+t[w_i][k_i],tk,res+str(t[w_i][k_i])+"+") or flag
                tk[k_i] = True
            flag = rek(w_i+1,s,tk,res) or flag
        return flag

    t_b = [True for _ in range(n)]
    return rek(0, 0, t_b)


tab = [[1,1,1,1,4,1],
       [1,1,1,1,1,1],
       [1,1,1,33,1,1],
       [1,1,1,1,1,1],
       [1,4,1,1,1,1],
       [3,1,1,1,2,1]
       ]

print(zad21(tab,13))