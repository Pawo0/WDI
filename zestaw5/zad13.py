def rec(x, result="", j=1):
    if x == 0:
        print(result[:-1])
        return
    for i in range(j,x+1):
        rec(x-i,result+str(i)+"+",i)

rec(10)