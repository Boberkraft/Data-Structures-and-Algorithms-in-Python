"""
Isabel has an interesting way of summing up the values in a sequence A of
n integers, where n is a power of two. She creates a new sequence B of half
the size of A and sets B[i] = A[2i]+A[2i+1], for i = 0,1,...,(n/2)−1. If
B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and
repeats the process. What is the running time of her algorithm?

So the function is called log n times (everytime data is halved by half)
and every call its doing a loop half the actuall size (log n)

So lets sum it

log n * log n = n
Complexity is O(n)
"""

a = 0
def weird_sum(A):
    global a

    B = []
    for i in range(len(A)//2):
        a += 1
        B.append(A[2*i] + A[2*i +1])

    if len(B) == 1:
        return B[0]
    return weird_sum(B)

if __name__ == '__main__':
    n = 2 ** 6
    A = list(range(n))
    print(len(A))
    print(weird_sum(A))
    print(sum(A))
    print(a)