from lista import Node as Parent


class Node(Parent):
    def __init__(self, val=None, id=None, next=None):
        Parent.__init__(self, val, next)
        self.id = id


def print_list(p):
    while p is not None:
        if p.val is not None:
            print(f"id:{p.id}, val:{p.val}", end=" -> ")
        p = p.next
    print("END")


def init(n=10):
    a = Node(0,n)
    for i in range(n-1,-1,-1):
        b = Node(0,i,a)
        a = b
    return a


def get(p,id):
    while p.next is not None:
        if p.next.id == id:
            return p.next.val
        elif p.next.id > id:
            break
        p = p.next()
    return None


def add(p,val,id):
    start = p
    while p.next is not None and p.next.id < id:
        p = p.next
    if p.next is not None and p.next.id == id:
        p.val = val
    elif p.next is not None and p.next.id > id:
        tmp = p.next
        p.next = Node(val,id,tmp)
    else:
        p.next = Node(val,id)
    return start


if __name__ == "__main__":
    p = init(3)
    g = Node(None,None,p)
    g = add(g,6,2)
    g = add(g,3,5)
    g = add(g,3,505)
    g = add(g,4,6)
    g = add(g,5,4)
    print_list(g)
