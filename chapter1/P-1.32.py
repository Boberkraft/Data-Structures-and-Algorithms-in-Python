# Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator

allowed = {'/', '*', '**', '+', '-'}
stack = [0]
res = 0

def add(cmd):
    global stack
    try:
        stack.append(float(cmd))
    except ValueError:
        if cmd != '=':
            stack.append(cmd)
        else:
            execute()
    if len(stack) > 2 and isinstance(stack[-1], float) and isinstance(stack[-2], str):
        execute()

def show(num):
    global res
    res = num
    print(num)

def execute():
    global stack, res, allowed
    res = 0
    error = False
    last_num = False
    try:
        for i in range(len(stack)):
            if isinstance(stack[i], str):
                if stack[i] not in allowed:
                    raise ValueError
                eval('show({} {} {})'.format(stack[i-1],
                                           stack[i],
                                           stack[i+1]))
    except ValueError:
        stack = [0]
        print('Error! restarting')
    else:
        stack = [res]


if __name__ == '__main__':
   while True:
       cmd = input(': ')
       add(cmd)




