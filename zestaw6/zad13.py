from lista import Node, print_list, init_rand


# usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio poprzedzających je elementów
def zad13(p):
   suma = 0
   p = Node(None,p) if p.val is not None else p
   res = p
   while p.next is not None:
      if p.next.val < suma:
         p.next = p.next.next
      else:
         suma += p.next.val
         p = p.next
   return res.next


if __name__ == "__main__":
   p = init_rand(10,1,30)
   print_list(p)
   p = zad13(p)
   print_list(p)