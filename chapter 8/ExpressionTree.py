from LinkedBinaryTree import LinkedBinaryTree


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

    def postfix(self):
        return self._postfix(self.root())

    def _postfix(self, p):
        ans = []
        if not self.is_leaf(p):
            ans.append(self._postfix(self.left(p)))
            ans.append(self._postfix(self.right(p)))
        ans.append(p.element())

        return ' '.join(ans)



def build_expression_tree(tokens):
    S = []
    for t in tokens:
        if t in '+-x*/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()

def build_expression_tree2(tokens):
  S = []
  for t in tokens:
    if t in '+-x*/':
      S.append(t)
    elif t not in '()':
      S.append(ExpressionTree(t))
    elif t == ')':
      right = S.pop()
      op = S.pop()
      left = S.pop()
      S.append(ExpressionTree(op, left, right))
    # we ignore a left parenthesis
  return S.pop()

def tokenize(raw):
  """Produces list of tokens indicated by a raw expression string.

  For example the string '(43-(3*10))' results in the list
  ['(', '43', '-', '(', '3', '*', '10', ')', ')']
  """
  SYMBOLS = set('+-x*/() ')    # allow for '*' or 'x' for multiplication

  mark = 0
  tokens = []
  n = len(raw)
  for j in range(n):
    if raw[j] in SYMBOLS:
      if mark != j:
        tokens.append(raw[mark:j])  # complete preceding token
      if raw[j] != ' ':
        tokens.append(raw[j])       # include this token
      mark = j+1                    # update mark to being at next index
  if mark != n:
    tokens.append(raw[mark:n])      # complete preceding token
  return tokens

# x = build_expression_tree('(((3+1)*4)/((9-5)+2))')
# print(x, '=', x.evaluate())
