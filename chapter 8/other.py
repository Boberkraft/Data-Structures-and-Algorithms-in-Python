def preorder_intent(T, p, d):
    print(2 * d * ' ' + str(p.element()))
    for c in T.children(p):
        preorder_intent(T, c, d + 1)


def preorder_label(T, p, d, path):
    label = '.'.join(str(j + 1) for j in path)
    print(2 * d * ' ' + label, p.element())
    path.append(0)
    for c in T.children():
        preorder_label(T, c, d + 1, path)
        path[-1] += 1
    path.pop()


def parenthesize(T, p):
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' ( ' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')


def disk_space(T, p):
    subtotal = p.element().space()
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal


def disk_space(T, p):
    subtotal = p.element().space()
    for c in T.children(p):
        subtotal += disk_space(T, c)
        return subtotal
