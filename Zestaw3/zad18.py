def how_long_is_odd_palindrome(t: list) -> int:
    length = len(t) - 1
    max_cnt = 0
    for i in range(length):
        if t[i] % 2 == 0:
            continue
        for j in range(length, 0, -1):
            cnt = 0
            while i <= length and j >= 0 and t[i] == t[j] and t[i] % 2 == 1:
                cnt += 1
                i += 1
                j -= 1
            max_cnt = max(ctn, max_cnt)
    return max_cnt



if __name__ == "__main__":
    tab = [0,2,4,1,5,3,5,3,5,2,1,8]
    print(how_long_is_odd_palindrome(tab))