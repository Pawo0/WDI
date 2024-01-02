def suma_szach(t,r1,r2) -> int:
    n = len(t)
    suma = 0
    suma -= t[r1[0]][r1[1]]*2 + t[r2[0]][r2[1]]*2
    for i in range(n):
        suma += t[r1[0]][i] + t[i][r1[1]]
        if i != r1[0] and i != r1[1]:
            suma += t[r2[0]][i] + t[i][r2[1]]
        elif i != r1[0]:
            suma += t[i][r2[1]]
        elif i != r1[1]:
            suma += t[r2[0]][i]

    return suma


# kij w to zadanie 
def zad1(t,r1,r2):
    n = len(t)
    poczatkowa_suma = suma_szach(t,r1,r2)
    def rek(r1,r2,ruch=""):
        if suma_szach(t,r1,r2) > poczatkowa_suma:
            return True
        if r1[0] == n or r1[1] == n or r2[0] == n or r2[1] == n:
            return False
        if ruch == "":
            return (rek((r1[0]+1,r1[1]),r2,"w1") or rek((r1[0],r1[1]+1),r2,"k1") or
                    rek(r1,(r2[0]+1,r2[1]),"w2") or rek(r1,(r2[0],r2[1]+1),"k2"))

        return (
            False if ruch != "w1" else rek((r1[0]+1,r1[1]),r2,ruch) or
            False if ruch != "k1" else rek((r1[0],r1[1]+1),r2,ruch) or
            False if ruch != "w2" else rek(r1,(r2[0]+1,r2[1]),ruch) or
            False if ruch != "k2" else rek(r1,(r2[0],r2[1]+1),ruch)
        )

    return rek(r1,r2)

tab = [ [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16] ]

print(zad1(tab,(3,3),(3,3)))