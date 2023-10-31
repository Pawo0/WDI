def rozklad(x):
    while x % 2 == 0:
        x /= 2
    while x % 3 == 0:
        x /= 3
    while x % 5 == 0:
        x /= 5
    if x == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    n = 1_000_000
    ile = 0
    for i in range(1, n+1):
        if rozklad(i):
            ile += 1

    print(ile)
