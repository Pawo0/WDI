def max_one_prime_factor(x: int) -> bool:
    i = 2
    while x != 1:
        cnt = 0
        while x % i == 0 and x != 1:
            x //= i
            cnt += 1
        if cnt > 1:
            return False
        i += 1
    return True


def product_sequence_with_one_prime_factor(t: list) -> int:
    length = len(t)
    max_cnt = 0
    for i in range(length-1):
        sum_product = t[i]
        cnt = 1
        if max_one_prime_factor(sum_product):
            for j in range(i + 1,length):
                sum_product *= t[j]
                if not max_one_prime_factor(sum_product):
                    break
                else:
                    cnt += 1
                    max_cnt = max(cnt, max_cnt)
    return max_cnt


tab = [2,23,33,35,7,4,6,7,5,11,13,22]

print(product_sequence_with_one_prime_factor(tab))