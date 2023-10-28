from random import randrange

def rand_tab(t):
    return [randrange(1,100,2) for _ in range(t)]


def difference_r_in_arith_sequences(x: list) -> int:
    cnt, max_cnt_inc, max_cnt_dec = 1, 0, 0
    r = x[1] - x[0]
    i = 1
    while i < len(x):
        if x[i] - x[i-1] == r:
            cnt += 1
        else:
            if r > 0:
                max_cnt_inc = max(max_cnt_inc, cnt)
            elif r < 0:
                max_cnt_dec = max(max_cnt_dec, cnt)
            r = x[i] - x[i-1]
            cnt = 2
        i += 1
    if r > 0:
        max_cnt_inc = max(max_cnt_inc, cnt)
    else:
        max_cnt_dec = max(max_cnt_dec, cnt)
    print("r > 0:",max_cnt_inc,"  |   r < 0: ", max_cnt_dec)
    return abs(max_cnt_inc-max_cnt_dec)


if __name__ == "__main__":
    tab = rand_tab(15)
    print(tab)
    print("difference", difference_r_in_arith_sequences(tab))