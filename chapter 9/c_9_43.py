"""
Explain how the k largest elements from an unordered collection of size n
can be found in time O(n log k) using O(k) auxiliary space.

Prepare a special priorityqueue that only have space for k elements. When inserting an element,
do upheap and after that drop the lowest A (might not work)

make minheap of first k elements,
and then compere next n - k elements with root of the heap. 
If its biger than root, call heapify(0)
"""
