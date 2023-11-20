from math import log10
from funkcje import czy_pierwsza


def closet_prime(n):
    for i in range(n,1,-1):
        if czy_pierwsza(i):
            return i


def divide(n):
    len_n = int(log10(n))+1
    