def increasing_sequence_equal_to_sum_of_indexes_bad(t: list) -> int:
    length = len(t)
    i = 1
    cnt, max_cnt = 1, 0
    sum_index, sum_value = 0, t[0]
    while i < length:
        if sum_index == sum_value:
            max_cnt = max(max_cnt, cnt)
        if t[i] > t[i-1]:
            sum_value += t[i]
            sum_index += i
            cnt += 1
        else:
            sum_value = t[i]
            sum_index = i
            cnt = 1
        print(f"liczba {t[i]}, index {i}, cnt {cnt}, sum_index {sum_index}, sum_value {sum_value}")
        i += 1
    return max_cnt


def increasing_sequence_equal_to_sum_of_indexes(t: list) -> int:
    length = len(t)
    max_cnt = 0
    for i in range(length-1):
        if t[i] < t[i + 1]:
            cnt = 1
            sum_i, sum_v = i, t[i]
            for j in range(i+1, length):
                if not t[j] > t[j-1]:
                    break
                else:
                    cnt += 1
                    sum_i += j
                    sum_v += t[j]
                    if sum_i == sum_v:
                        max_cnt = max(max_cnt, cnt)
    return max_cnt


tab1 = [1,3,2,3,3,3,4,5,12,13]
print(increasing_sequence_equal_to_sum_of_indexes(tab1))