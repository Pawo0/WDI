from lista import Node, print_list


def increase(p,by):
    if p.next is not None:
        p.val = p.val + increase(p.next,by)  # dodaje do cyfry dziesiatki zsumowane nizej
    else:
        p.val = p.val + by # dodaje "by" do ostatniej liczby
    if p.val >= 10: # ucina 'ogonek' i przesyła go wyżej
        r = p.val // 10
        p.val = p.val%10
        return r
    return 0


def init_number(n):
    a = Node(n%10)
    n //= 10
    while n != 0:
        digit = n%10
        b = Node(digit,a)
        a = b
        n //= 10
    return a


if __name__ == "__main__":
    p = init_number(2498)
    print_list(p)
    increase(p,32)
    print_list(p)