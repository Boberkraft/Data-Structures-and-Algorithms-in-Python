"""
Postfix notation is an unambiguous way of writing an arithmetic expression
without parentheses. It is defined so that if “(exp1)op(exp2)” is a
normal, fully parenthesized expression whose operation is op, the postfix
version of this is “pexp1 pexp2 op”, where pexp1 is the postfix version of
exp1 and pexp2 is the postfix version of exp2. The postfix version of a single
number or variable is just that number or variable. For example, the
postfix version of “((5+2) ∗ (8−3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe
a nonrecursive way of evaluating an expression in postfix notation.

after making it i checked google for more examples, and... i found out that i got the whole idea wrong. opss.
"""



def operation(s):
    if s == '+':
        return lambda x, y: x + y
    if s == '-':
        return lambda x, y: x - y
    if s == '/':
        return lambda x, y: x / y
    if s == '*':
        return lambda x, y: x * y
    return False


def evaluate(raw):
    numbers = [] # my stack
    data = raw.split()

    way = 0
    last_num = False
    for exp in data:
        op = operation(exp)

        if op is False:
            numbers.append(int(exp))
            last_num = True
        else:

            if not last_num or len(numbers) - way == 1:
                way = 0
            s = numbers.pop()
            while len(numbers) > way:
                s = op(numbers.pop(), s)
            if last_num:
                way += 1
            numbers.append(s)


            last_num = False
    return numbers[0]

# “(((5 + 5) + (2 + 5) + (5 - 2)) * 2) + 100”
#          10        7         2
#                 20 * 2
#                 40
#                 140
ans = evaluate("5 5 + 2 5 + 5 2 - + 2 * 100 +")
print(ans)
