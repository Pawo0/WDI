def mult_3_and_5(x):
    result = 0
    for i in range(x):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i
    return result

print(mult_3_and_5(1000))