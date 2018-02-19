"""
Note that the build expression tree function of the ExpressionTree class
is written in such a way that a leaf token can be any string; for example,
it parses the expression (a*(b+c)) . However, within the evaluate
method, an error would occur when attempting to convert a leaf token to
a number. Modify the evaluate method to accept an optional Python dictionary
that can be used to map such string variables to numeric values,
with a syntax such as T.evaluate({ a :3, b :1, c :5}). In this way,
the same algebraic expression can be evaluated using different values.
"""
from ExpressionTree import ExpressionTree


def build_expression_tree(tokens, variables=None):
    S = []
    for t in tokens:
        if t in '+-x*/':
            S.append(t)
        elif t not in '()':
            if variables is None:
                S.append(ExpressionTree(t))
            else:
                S.append(ExpressionTree(variables[t]))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()


x = build_expression_tree('(((3+1)*4)/((9-5)+2))')
print(x, '=', x.evaluate())

vars = dict(a='3', b='1', c='4', d='9', e='5', f='2')

x = build_expression_tree('(((a+b)*c)/((d-e)+f))', vars)
print(x, '=', x.evaluate())
