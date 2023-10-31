def iloczyn(x):
    min_roznica = x
    liczby = ()
    for i in range(1, x//2+1):
        if x % i == 0:
            roznica = abs(i-x//i)
            if roznica < min_roznica:
                min_roznica = roznica
                liczby = (i, x//i)
    return liczby

if __name__ == "__main__":
    print(f"30 = {iloczyn(30)}")
    print(f"120 = {iloczyn(120)}")

