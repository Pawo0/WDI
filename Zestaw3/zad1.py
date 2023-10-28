from math import log

def change_sys(n,sys):
    length = int(log(n,sys))
    chars = "0123456789ABCDEF"
    numbers = [0 for _ in range(length+1)]
    i = 0
    while n > 0:
        numbers[length-i] = chars[n % sys]
        n //= sys
        i += 1
    return numbers

print(change_sys(985,16))