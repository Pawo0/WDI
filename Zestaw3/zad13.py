from random import randint


def rand_tab(n: int) -> list:
    return [randint(10, 100) for _ in range(n)]


def reversed_sequence(x: list) -> int:
    length = len(x) - 1
    max_cnt = 0
    for i in range(length):
        for j in range(length, 0, -1):
            cnt = 0
            while i <= length and j >= 0 and x[i] == x[j]:
                cnt += 1
                i += 1
                j -= 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt


if __name__ == "__main__":
    tab = rand_tab(100)
    print(tab)
    print(reversed_sequence(tab))
