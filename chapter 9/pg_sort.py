from PriorityQueue import PriorityQueue


def pg_srot(C):
    n = len(C)
    P = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)

