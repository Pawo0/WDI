def czy_zaprz(x, y):
    return (sum([i for i in range(1, int(x / 2) + 1) if x % i == 0]) == y and
            sum([i for i in range(1, int(y / 2) + 1) if y % i == 0])) == x


for i in range(1, 300):
    for j in range(i + 1, 300):
        if czy_zaprz(i, j):
            print(i, j)

