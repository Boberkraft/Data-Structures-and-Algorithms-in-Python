"""
Find the value of the arithmetic expression associated with each subtree
of the binary tree of Figure 8.8.

((((3+1)*3)/((9-5)+2))-((3*(7-4))+6)) = -13.0
"""

from ExpressionTree import build_expression_tree

x = build_expression_tree('((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))')
print(x, '=', x.evaluate())