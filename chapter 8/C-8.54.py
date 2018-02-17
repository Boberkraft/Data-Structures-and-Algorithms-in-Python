"""
Design an algorithm for drawing general trees, using a style similar to the
inorder traversal approach for drawing binary trees.
"""

counter = 0


def draw(tree, p, d):
    kids = tree.children(p)
    for kid in kids[0:len(kids) // 2]:
        draw(tree, kid, d + 1)
    p.setY(d)
    p.setX(counter)
    for kid in kids[len(kids) // 2:]:
        draw(tree, kid, d + 1)
