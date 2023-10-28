def number_length(x):
    i = 0
    while x > 0:
        x //= 10
        i += 1
    return i

def are_the_same_numbers(x,y):
    tab_x = [0 for _ in range(number_length(x))]
    tab_y = [0 for _ in range(number_length(y))]
    index = 0
    while x > 0:
        tab_x[index] = x%10
        x //= 10
        index+=1
    index = 0
    while y > 0:
        tab_y[index] = y%10
        y //= 10
        index+=1
    tab_x.sort()
    tab_y.sort()
    if tab_x == tab_y:
        return True
    return False

print(are_the_same_numbers(1255,5125))