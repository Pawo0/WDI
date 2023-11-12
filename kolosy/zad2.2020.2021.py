from math import inf


def na_dzies(T) -> int:
    pot = len(T) - 1
    wynik = 0
    i = 0
    while pot >= 0:
        if T[i] == 1:
            wynik += pow(2,pot)
        i += 1
        pot -= 1
    return wynik


def distance(T):
    n = len(T)
    i = 0
    minimal = (inf,inf)
    maxymal = (-1,-1)
    while i < n:
        liczba = na_dzies(T[i])
        if liczba < minimal[0]:
            minimal = (liczba, i)
        if liczba > maxymal[0]:
            maxymal = (liczba, i)
        i += 1
    odleglosc = abs(maxymal[1]-minimal[1])
    return odleglosc


tab = [1,0,0,1]
print(na_dzies(tab))