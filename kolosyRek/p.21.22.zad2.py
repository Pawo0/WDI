def czy_nachodzi(p1,p2):
    return False

def zad2(T):
    Wybrane_i = [None]*len(T)
    def rek(i,suma, Wybrane_i, ile):
        if suma == 2022:
            return True
        if suma > 2022:
            return False
        if i == len(T):
            return False
        for j in range(ile):
            if czy_nachodzi(T[i],T[Wybrane_i[j]]):
                break
        else:
            if rek(i+1,suma,Wybrane_i,ile):
                return True
            Wybrane_i[ile] = i
            return rek(i+1,suma+abs(T[i][1]-T[i][0]),Wybrane_i,ile+1)
        return rek(i+1,suma,Wybrane_i,ile)
    return rek(0,0,Wybrane_i,0)