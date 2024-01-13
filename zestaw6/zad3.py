from lista import Node, print_list


# ja wiem jak to wyglada, ale dziala
def scal(p,q):
    if p.next is None:
        p.next = q.next
        return p
    if q.next is None:
        return p
    if p.next.val < q.next.val:
        scal(p.next,q)
        return p
    if p.next.val > q.next.val:
        tmp = p.next
        p.next = q.next
        q.next = q.next.next
        p.next.next = tmp
        scal(p.next,q)
        return p
    if p.next.val == q.next.val:
        scal(p.next,q.next)
        return p


def scal2(p,q):
    """przekazuj bez guardiana"""
    if p is None:
        return q
    if q is None:
        return p
    if p.val < q.val:
        p.next = scal2(p.next,q)
        return p
    elif p.val > q.val:
        q.next = scal2(p,q.next)
        return q
    else:
        # są równe
        p.next = scal2(p.next,q.next)
        return p

def init(n=10,by=1):
    """tworzy liste do n rosnacą by"""
    a = Node(n)
    for i in range(n-by,-1,-by):
        b = Node(i,a)
        a = b
    return a


def create_p_q():
    p = init(10, 3)
    p = Node(None, p)
    print_list(p)

    q = init(30, 5)
    q = Node(None, q)
    print_list(q)
    return p, q

def test_pierwszej():
    p, q = create_p_q()

    res = scal(p, q)
    print_list(res)


def test_drugiej():
    p, q = create_p_q()

    res2 = scal2(p.next, q.next)
    print_list(res2)


if __name__ == "__main__":

    test_pierwszej()
    print("*"*30,"\n")
    test_drugiej()

