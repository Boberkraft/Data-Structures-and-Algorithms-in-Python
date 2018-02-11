"""
Our definition of the level numbering function f(p), as given in Section
8.3.2, began with the root having number 0. Some authors prefer
to use a level numbering g(p) in which the root is assigned number 1, because
it simplifies the arithmetic for finding neighboring positions. Redo
Exercise R-8.18, but assuming that we use a level numbering g(p) in
which the root is assigned number 1.

How this is this simpler?
def root():
    return array[0]

def parent(p):
    return floor((g(p))/2)
    
def left(p):
    return array[2 f(p)]
    
def right(p):
    return array[2 f(p) + 1]

def is_leaf(p)
    if 2 f(p) + 1 > n:
        if 2 f(p) + 1 is None:
            if 2 fp(p) is None:
                return True
    return False
    
def is_root(p):
    return p == self.root()
     
"""
