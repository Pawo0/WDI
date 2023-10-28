def increasing_sequence(x: list) -> int:
    cnt, max_cnt, i = 1, 1, 1
    while i < len(x):
        if x[i] > x[i-1]:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 1
        i += 1
    return max(cnt, max_cnt)

tab = [4,5,7,2,11,8,9,13,20,20,21,22,25]

print(increasing_sequence(tab))