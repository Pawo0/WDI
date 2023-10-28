def liczba_z_ciagu(n=10):
    ciag = [0] * n
    while True:
        x = int(input("Podaj liczbe:"))
        if x == 0:
            break
        i = 0
        while i < len(ciag):
            if x > ciag[i]:
                x, ciag[i] = ciag[i], x
            i += 1

    return ciag[-1]

print(liczba_z_ciagu(5))