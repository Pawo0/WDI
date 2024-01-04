def nwd(a,b):
    if b == 0:
        return a
    return nwd(b,a%b)

def nwd3(z):
    a = z[0]
    b = z[1]
    c = z[2]
    return nwd(nwd(a,b),c)

def trojki(T):

    def rek(i,ost,zbior):
        if i == len(T):
            return False
        if len(zbior) == 3:
            if nwd3(zbior) == 1:
                print(zbior)
                return True
            return False
        if ost != 0:
            rek(i+1,0,zbior)
        rek(i+1,i,zbior+[T[i]])

    return rek(0,-1,[])


print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)