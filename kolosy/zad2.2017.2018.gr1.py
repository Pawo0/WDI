def func(t):
    n = len(t)
    najdl = 0
    for i in range(n-1):
        sum_ind = i
        sum_el = t[i]
        for j in range(i+1,n):
            sum_ind += j
            sum_el += t[j]
            if t[j-1] >= t[j]:
                break
            if sum_ind == sum_el:
                dl = j - i + 1
                najdl = max(najdl,dl)
    return najdl if najdl > 1 else 0

#      0 1 2 3 4 5 6 7 8
tab = [5,2,4,3,4,5,8,9,4]
print(func(tab))