EPS = 1e-8

def zad19():
    e, e_chk, fact, i = 1, 0, 1, 1
    while abs(e_chk-e) > EPS:
        e_chk = e
        fact *= i
        e += 1/fact
        i += 1
    return e

if __name__ == "__main__":
    print(zad19())