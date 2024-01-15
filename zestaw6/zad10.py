from lista import Node, init_number, print_list


def linked_to_int(p:Node):
    p = Node(None,p) if p.val is not None else p # guard
    res = 0
    while p.next is not None:
        digit = p.next.val % 10
        res = res*10 + digit
        p = p.next
    return res


def int_to_linked(n:int):
    s = Node(n%10)
    n //= 10
    while n != 0:
        s = Node(n%10,s)
        n //= 10
    return s


def list_sum(p,q):
    l1 = linked_to_int(p)
    l2 = linked_to_int(q)
    res = l1 + l2
    result = int_to_linked(res)
    return result


if __name__ == "__main__":
    p = init_number(27)
    q = init_number(14)
    r = list_sum(p,q)
    print_list(r)

