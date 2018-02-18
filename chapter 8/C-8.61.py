"""
Give an alternative implementation of the build expression tree method
of the ExpressionTree class that relies on recursion to perform an implicit
Euler tour of the tree that is being built.
"""

from LinkedBinaryTree import LinkedBinaryTree
import re
from copy import copy


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super(ExpressionTree, self).__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be string')
        self._add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(')')

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val


def build_expression_tree(tokens):
    tokens = copy(tokens)
    print('-' * 5)

    striping = True
    while striping and (tokens[0] == '(' and tokens[-1] == ')'):
        tokens = tokens[1:len(tokens) - 1]
        print('Transforming to: ', end='')
        print("Range", ''.join(tokens))
        counter = 0
        for token in tokens:
            if token == '(':
                counter += 1
            if token == ')':
                counter -= 1
            if counter < 0:
                tokens = ['('] + tokens + [')']
                print('Untransforming: bracket not matched')
                striping = False
                break

    print("Range", ''.join(tokens))

    counter = 0
    if len(tokens) == 1:
        # its a single number
        return ExpressionTree(tokens[0])
    for i, t in enumerate(tokens):
        if t == '(':
            counter += 1
        elif counter == 0 and t in '+-/*':
            # its something like this (2+1)/(4*3)
            print("Spliting to half:", ''.join(tokens))
            print(''.join(tokens[:i]), '<=', t, '=>', ''.join(tokens[i + 1:]))
            print('i =', i)
            left = build_expression_tree(tokens[:i])
            right = build_expression_tree(tokens[i + 1:])
            return ExpressionTree(t, left, right)
        elif t == ')':
            counter -= 1


def tokenize1(raw):
    regex = r"[0-9]+|\(|\)|[-/+*x]"

    matches = re.finditer(regex, raw)
    return [match.group() for match in matches]


tokens = tokenize1('(((3+1)*4)/((9-5)+2))')
"""
((3+1)*4)       ((9-5)+2))
(3+1)      4    (9-5)  2

3  1                9   5
"""
print(' '.join(tokens))

tree = build_expression_tree(tokens)
print('*'*15)
print('Evaluated!')
print(tree, '=', tree.evaluate())
