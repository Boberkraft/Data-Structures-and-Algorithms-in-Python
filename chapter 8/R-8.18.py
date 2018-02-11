"""
Let T be a binary tree with n positions that is realized with an array representation
A, and let f() be the level numbering function of the positions
of T, as given in Section 8.3.2. Give pseudo-code descriptions of each of
the methods root, parent, left, right, is leaf, and is root.

def root():
    return array[0]

def parent(p):
    return floor((f(p) - 1)/2)
    
def left(p):
    return array[2 f(p) + 1]
    
def right(p):
    return array[2 f(p) + 2]

def is_leaf(p)
    if 2 f(p) + 2 > n:
        if 2 f(p) + 2 is None:
            if 2 fp(p) + 1 is None:
                return True
    return False
    
def is_root(p):
    return p == 0
     
     
"""
