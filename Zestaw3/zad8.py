tab = [21,8,14,23,2,1,4,3]


def jump_by_factor_to_last(x: list) -> bool:
    looking_for = len(x) - 1
    first_number = x[0]
    factor = 2
    while factor <= first_number:
        if first_number % factor == 0:
            if factor == looking_for:
                return True
            first_number //= factor
        else:
            factor += 1
    return False

print(jump_by_factor_to_last(tab))