"""
Assume that we are using a linked representation of a complete binary
tree T, and an extra reference to the last node of that tree. Show how to
update the reference to the last node after operations add or remove min
in O(log n) time, where n is the current number of nodes of T. Be sure
and handle all possible cases, as illustrated in Figure 9.12.

If p is the root of T, then f (p) = 0.
• If p is the left child of position q, then f (p) = 2 f (q)+1.
• If p is the right child of position q, then f (p) = 2 f (q)+2.



                0 
          1           2                             
        3    4     5     6                                
      7  8  9 10 11 12 13 14
      
      12 - 1  -> prawo
      5 - 1 -> lewo
      2 - 1 -> prawo
      
"""


def calculate_new_tail():
    mov = []
    to_go = len(self)
    while to_go > 0:
        mov.append((to_go + 1)% 2)
        to_go = (to_go - 1) // 2

    tail = self.root()
    for _ in mov:
        move = mov.pop() # 1 if right, 0 if left
        if move == 1:
            tail = tail.right(tail)
        else:
            tail = tail.right(tail)

