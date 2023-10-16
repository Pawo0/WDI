def dzielenie(x,y,n):
    wynik = ""
    wynik += str(x // y) + "."
    for i in range(n+1):
        x = x % y * 10
        wynik += str(x // y)
    return wynik

print(dzielenie(10,7,100))
print(f"{10/7:.100f}")