def arithmetic_sequence(x: list) -> int:
    r = x[1] - x[0]
    ctn, max_ctn, i = 1, 1, 1
    while i < len(x):
        if x[i] - x[i-1] == r:
            ctn += 1
        else:
            max_ctn = max(ctn, max_ctn)
            r = x[i] - x[i-1]
            ctn = 2
        i += 1
    return max(ctn, max_ctn)

tab = [4,2,0,11,12,14,5,13,20,20,21,22,23]

print((arithmetic_sequence(tab)))