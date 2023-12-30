def zad2(t1,t2):
    def rek(i=0,s1=0,s2=0,cnt1=0,cnt2=0):
        if s1 == s2 and cnt1 == cnt2 and s1 != 0:
            return cnt1
        if i == len(t1):
            return 0
        return max(rek(i+1,s1,s2,cnt1,cnt2), rek(i+1,s1+t1[i],s2,cnt1+1,cnt2),
                   rek(i+1,s1,s2+t2[i],cnt1,cnt2+1), rek(i+1,s1+t1[i],s2+t2[i],cnt1+1,cnt2+1))
    return rek()


t1 = [2, 4, 3, 8]
t2 = [1, 5, 3, 10]

print(zad2(t1,t2))