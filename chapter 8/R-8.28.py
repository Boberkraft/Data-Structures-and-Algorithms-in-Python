"""
What is the running time of parenthesize(T, T.root( )), as given in Code
Fragment 8.25, for a tree T with n nodes?

def parenthesize(T, p):
    ”””Print parenthesized representation of subtree of T rooted at p.”””
    print(p.element( ), end= ) # use of end avoids trailing newline
    if not T.is leaf(p):
        first time = True
        for c in T.children(p):
            sep = ( if first time else , # determine proper separator
            print(sep, end= )
            first time = False # any future passes will not be the first
            parenthesize(T, c) # recur on child
        print( ) , end= ) # include closing parenthesis
Assume printing is O(1).
T.is_leaf(p) is O(1)
O(n)
because each position of T, with the exception of the root, is a child of
another position.
"""

