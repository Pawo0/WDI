def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

def palindrome_product(digits):
    first = 10 ** (digits-1)
    last = 10 ** digits - 1
    x = first
    result = 0
    while x <= last:
        y = first
        while y <= last:
            number = x * y
            if is_palindrome(number) and number > result:
                result = number
            y += 1
        x += 1
    return result


print(palindrome_product(3))