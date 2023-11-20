def func(x,y):
    for podst in range(2,16+1):
        tab = [0] * podst
        x_copy, y_copy = x, y
        flag = True
        while x_copy != 0:
            cyfra = x_copy % podst
            tab[cyfra] = 1
            x_copy //= podst
        while y_copy != 0:
            cyfra = y_copy % podst
            if tab[cyfra] == 1:
                flag = False
                break
            y_copy //= podst
        if flag:
            return podst

print(func(123,522))