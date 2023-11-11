def fib(x,y,szukana):
    while x < szukana+1:
        x, y = y, x+y
        if x == szukana:
            return True
    return False


szukana = 2023

min_suma = 2023
for i in range(1,szukana):

    for j in range(i,szukana):
        if fib(i,j,szukana):
            if i+j < min_suma:
                min_suma = i+j
                pi = i
                pj = j

print(min_suma,pi,pj)
print(f"Wynik {szukana} mozna osiagnac przy doborze liczb {pi}, {pj} - "
      f"które sumują się do {min_suma}")