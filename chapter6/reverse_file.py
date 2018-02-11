from ArrayStack import ArrayStack


def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
    output = open(filename, 'w')
    while len(S):
        output.write(S.pop() + '\n')
    output.close()

if __name__ == '__main__':
    reverse_file('test')