from math import sqrt

EPS = 1e-12
def granica_a_g(x,y):
    while abs(x-y) > EPS:
        x, y = sqrt(x*y), (x + y) / 2.0
    return x

def zad20():
    print(granica_a_g(17,444))


if __name__ == "__main__":
    zad20()