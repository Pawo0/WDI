from lista import Node, print_list


def scal(p,q):
    p = Node(None,p)
    q = Node(None,q)
    start = p.next
    while p.next is not None and q.next is not None:
        if q.next.val < p.next.val:
            tmp = p.next
            p.next = q.next
            p.next.next = tmp
            q = q.next
        else:
            p = p.next
    return start


def init(n=10,by=1):
    a = Node(n)
    for i in range(n-by,-1,-by):
        b = Node(i,a)
        a = b
    return a


p = init(10,3)
print_list(p)
q = init(30,5)
print_list(q)

res = scal(p,q)
print_list(res)