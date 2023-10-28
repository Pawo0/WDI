from random import randint


def random_numbers_list(n = 10):
    tab = [0] * n
    i = 0
    while i < n:
        tab[i] = randint(1,1001)
        i += 1
    return tab


def odd_number_in_numbers(x: list) -> bool:
    for i in x:
        flag = True
        while i > 0:
            if i % 2 == 0:
                flag = False
            i //= 10
        if flag:
            return True
    return False


if __name__ == "__main__":
    ctn = 1
    while True:
        tab = random_numbers_list()
        print(tab, odd_number_in_numbers(tab), ctn)
        if odd_number_in_numbers(tab):
            break
        ctn += 1
