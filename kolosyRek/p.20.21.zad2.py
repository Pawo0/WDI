def czy_samo(s):
    samo = ["a", "e", "o", "i", "u", "y"]
    if s in samo:
        return 1
    return 0

def cutting(s):

    def rek(s,i,k,cnt):
        if cnt == 2:
            return 0
        if i == len(s):
            if cnt == 1:
                return 1
            return 0
        if cnt == 1:
            return rek(s,i+1,k,cnt+czy_samo(s[i])) + rek(s,i+1,i,czy_samo(s[i]))
        return rek(s,i+1,k,cnt+czy_samo(s[i]))


    return rek(s,0,0,0)

print(cutting("student"))

