"""
Consider a variant of Exercise C-5.16, in which an array of capacity N is
resized to capacity precisely that of the number of elements, any time the
number of elements in the array goes strictly below N/4. Give a formal
proof that any sequence of n append or pop operations on an initially
empty dynamic array takes O(n) time.

Also you cant do n pops on initially empty dynamic array.
................................ 32
........ 8

at 16 it expands to 32
and to shrink it needs to go from 32 to 8.

Consider worst case.
8 -> 16 -> 32
now pops
32 -> 8
and expands again
8->16
and pops again
18 - > 4

As you can see everyt shrinking takes care of two expands. 
Now lets take cyber dollars into action.
making array of size n -> n cyber dollars
moving element -> 1 cyber dollar
append, pop -> 1 cyber dollar

Or right. We know that appending elements generate 4 cyber dollars 
(i have covered it in exercize before)

After shringing the array from 4k to k it needs to have 3k cyber dollars if user would want append element:
costs:
2k cyber dollars -> creating array of double size
k cyber dollars -> moving actual elements to new array
+ 1 dollar(lets ignore it)

So pop operation need to cost 4 cyber dollars (3 mentioned before + one for pop operation)

I have covered the worst case, so if you pop futher you lose less cyber dollar and that is + for you.
"""

from dynamicarray import DynamicArray

class NewArray(DynamicArray):
    def pop(self):
        el = self[-1]
        self._A[self._n] = None
        self._n -= 1
        if self._n <= self._capacity/4:
            # shrink the array
            self._resize(self._n)
        return el

