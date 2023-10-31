def czy_palindrom(n):
    n_og = n
    n_rev = 0
    while n > 0:
        cyfra = n % 10
        n_rev = n_rev * 10 + cyfra
        n //= 10
    return n_og == n_rev

def czy_palindrom_bin(n):
    n_og = n
    n_rev = 0
    while n > 0:
        cyfra = n % 2
        n_rev = n_rev * 2 + cyfra
        n //= 2
    return n_og == n_rev



if __name__ == "__main__":
    print(czy_palindrom(53235))
    print(czy_palindrom_bin(5))
