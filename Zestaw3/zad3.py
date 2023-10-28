from math import isqrt
def sito_eratostenesa(n):
    liczby = [i for i in range(n+1)]
    i = 2
    while i <= isqrt(n):
        j = i + i
        while j < len(liczby):
            liczby[j] = 0
            j += i
        i += 1
    return liczby[2:]


if __name__ == "__main__":
    prime = sito_eratostenesa(100)
    for i in prime:
        if i != 0:
            print(i, end=" ")
