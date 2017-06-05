"""
Consider an implementation of a dynamic array, but instead of copying
the elements into an array of double the size (that is, from N to 2N) when
its capacity is reached, we copy the elements into an array with 
N/4
additional cells, going from capacity N to capacity N +
N/4. Prove that
performing a sequence of n append operations still runs in O(n) time in
this case.

Lets assume your array size is 100.
You make appen
this append gives new +25 cells
append again, and it gives +32 cells
So this means everytime you add 1/4 cells more than append before.
So every cell needs to generate money to support 1+1/4 futhure itself. 

let us assume that growing the array from size k to size 2k requires 2k cyberdollars
for the time spent initializing the new array.
If the array expands 2x the current size, every new cell need to support 2 futhure 
cells that will be apended. 
 
So its needs 2 dollars to initialize new array + 2 dollar to move to move itself 
and one from older generation.
Overall its initalizing n elements takes 2n + 2n cyber dolars. 4n is O(n)

Now lets look at new implementation.
Creating new array 2 cyber dollars
every cell needs to generate money to support 1+1/4 futhure itself.

Overall its initalizing n elements takes 2n + n(1+1/4) cyber dolars. 3 1/4 n < c*n for c = 5.It is aO(n)
 
"""
from dynamicarray import DynamicArray
from math import ceil


class NewDynamicArray(DynamicArray):
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(self._capacity + ceil(self._capacity/4))
        self._A[self._n] = obj
        self._n += 1


