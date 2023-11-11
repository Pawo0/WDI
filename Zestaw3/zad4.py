from pisemne import dodawanie, mnozenie

def euler():
    e = 1
    s = 1
    fact = 2
    while s > 0:
        e += s
        s /= fact
        fact += 1
    return e


def accurate_euler(x):
    e = [0 for _ in range(x+1)]
    s = [0 for _ in range(x+1)]
    s[0] = 1
    fact = 1
    while True:
        s = mnozenie(s,fact)
        break
        # xd






