def czy_inikalna(n):
    unikalna = n % 10
    n //= 10
    while n > 0:
        if n % 10 == unikalna:
            return False
        n //= 10
    return True

if __name__ == "__main__":
    print(czy_inikalna(1234))
    print(czy_inikalna(4121))
    print(czy_inikalna(44))
    print(czy_inikalna(69))