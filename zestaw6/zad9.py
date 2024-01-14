from lista import Node, print_list


def increase(p,by):
    if p.next is None:
        if p.val + by >= 10:
            p.val = 0
            return 1
        p.val = p.val + by
        return 0
    p.val = p.val + increase(p.next,by)
    if p.val >= 10:
        p.val = 0
        return 1
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
    p = init_number(2434)
    print_list(p)
    increase(p,1)
    print_list(p)