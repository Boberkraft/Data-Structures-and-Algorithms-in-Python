"""
Given a heap T and a key k, give an algorithm to compute all the entries
in T having a key less than or equal to k. For example, given the heap of
Figure 9.12a and query k = 7, the algorithm should report the entries with
keys 2, 4, 5, 6, and 7 (but not necessarily in this order). Your algorithm
should run in time proportional to the number of entries returned, and
should not modify the heap

def ls_or_rq(index, val):
    if len(self) > index and self.data[index] <= val:
        print(self.data[index])
        ls_or_rq(self.left(index), val)
        ls_or_rq(self.right(index), val)
        
invoke this method on the index 0.
"""
