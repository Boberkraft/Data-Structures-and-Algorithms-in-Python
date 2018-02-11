"""
Implement a program that can input an expression in postfix notation (see
Exercise C-6.22) and output its value.

So describe doesnty mean implement :p
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
        else:
            a = numbers.pop()
            s = op(numbers.pop(), a)
            numbers.append(s)
    return numbers[0]

ans = evaluate("15 7 1 1 + - / 3 * 2 1 1 + + - ")

print(ans)

