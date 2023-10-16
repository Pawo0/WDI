def ciag(x):
    krok = 0
    while x != 1:
        x = (x%2) * (3*x+1) + (1-x%2) * x/2
        krok += 1
    return krok

def zad16():
    max = 0
    odp = 0
    for i in range(2,10001):
        max_krokow = ciag(i)
        if max_krokow > max:
            odp = i
            max = max_krokow

    print(odp,ciag(odp))

if __name__ == "__main__":
    zad16()