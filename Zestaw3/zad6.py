from random import randint


def random_numbers_list(n: int = 10, x: int = 1, y: int = 1001) -> list:
    """n = length, x = first, y = last
    """
    tab = [0] * n
    i = 0
    while i < n:
        tab[i] = randint(x,y)
        i += 1
    return tab


def odd_digits_in_numbers(x: list) -> bool:
    for i in x:
        flag = False
        while i >0:
            if i % 2 == 1:
                flag = True
            i //= 10
        if not flag:
            return False
    return True


if __name__ == "__main__":
    ctn = 1
    while True:
        tab = random_numbers_list()
        print(tab, odd_digits_in_numbers(tab), ctn)
        if odd_digits_in_numbers(tab):
            break
        ctn += 1
