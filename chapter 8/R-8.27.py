"""
Give the output of the function parenthesize(T, T.root( )), as described
in Code Fragment 8.25, when T is the tree of Figure 8.8.

- ( / ( * ( + ( 3, 1), 3), + ( - ( 9, 5), 2)), + ( * ( 3, - ( 7, 4)), 6))
"""
from ExpressionTree import build_expression_tree
from other import parenthesize
x = build_expression_tree('(((3+1)*3)/((9-5)+2))-((3*(7-4))+6))')
print(x, '=', x.evaluate())
parenthesize(x,x.root())

