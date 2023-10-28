from math import sqrt
def prime(n):
    if n == 2 and n == 3:
        return True
    if n % 2 == 0 and n % 3 == 0:
        return False
    i = 5
    while i < sqrt(n):
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True

def prime_factors(x):
    i = 2
    while i <= x:
        if prime(i):
            while x % i == 0:
                print(i, end=" ")
                x //= i
        i += 1

if __name__ == "__main__":
    prime_factors(600851475143)