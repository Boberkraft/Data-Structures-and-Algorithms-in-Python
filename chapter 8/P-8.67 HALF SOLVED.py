"""
A slicing floor plan divides a rectangle with horizontal and vertical sides
using horizontal and vertical cuts. (See Figure) A slicing floor plan
can be represented by a proper binary tree, called a slicing tree, whose
internal nodes represent the cuts, and whose external nodes represent the
basic rectangles into which the floor plan is decomposed by the cuts. (See
Figure 8.25b.) The compaction problem for a slicing floor plan is defined
as follows. Assume that each basic rectangle of a slicing floor plan is
assigned a minimum width w and a minimum height h. The compaction
problem is to find the smallest possible height and width for each rectangle
of the slicing floor plan that is compatible with the minimum dimensions
of the basic rectangles. Namely, this problem requires the assignment of
values h(p) and w(p) to each position p of the slicing tree such that:



w(p) = |        w        => if p is a leaf whose basic rectangle has min width of w
       
       | max(w(l), w(r)) => if p is an internal position, assosiated with a horizontal
                            cut, with left child l and right child r
       
       | w(l) + w(r)     => if p is an internal position, assosiated with a 
                            vertical cut, with child l and right child r
                        
                        
                        
h(p) = |        h        => if p is a leaf whose basic rectangle has min height of h
       
       |   h(l) + h(r)   => if p is an internal position, assosiated with a horizontal
                            cut, with left child l and right child r
       
       | max(h(l), h(r)) => if p is an internal position, assosiated with a 
                            vertical cut, with child l and right child r
                            
                            
    
Design a data structure for slicing floor plans that supports the operations:

• Create a floor plan consisting of a single basic rectangle.

• Decompose a basic rectangle by means of a horizontal cut.

• Decompose a basic rectangle by means of a vertical cut.

• Assign minimum height and width to a basic rectangle.

• Draw the slicing tree associated with the floor plan.

• Compact and draw the floor plan.

+---------------+----------------+                          
|      E        |      F         |                          
|               |                |    
|-----------+---+-------+--------+              
|           |           |        |         
|           |           |        |              
|           |           |        |          
|           |    C      |   D    |        
|    A      |           |        |      
|           |           |        |            
|           |-----------+--------|     
|           |                    |    
|           |          B         |  
+-----------+--------------------+                           


                 +---+
                 |   |
        +------> | _ | <----------------------+
        |        |   |                        |
        |        +---+                        |
        |                                     |
      +-+-+                                 +-+-+
      |   |                                 |   |
  +-> | | | <-+                         +-> | | | <-+
  |   |   |   |                         |   |   |   |
  |   +---+   |                         |   +---+   |
+-+-+       +-+-+                     +-+-+       +-+-+
|   |       |   |                     |   |       |   |
| A |   +-> | _ | <-+                 | E |       | F |
|   |   |   |   |   |                 |   |       |   |
+---+   |   +---+   |                 +---+       +---+
      +-+-+       +-+-+
      |   |       |   |
      | B |   +-> | | | <-+
      |   |   |   |   |   |
      +---+   |   +---+   |
            +-+-+       +-+-+
            |   |       |   |
            | C |       | D |
            |   |       |   |
            +---+       +---+
            
i dont know how to draw it using console help
"""

from LinkedBinaryTree import LinkedBinaryTree
from copy import deepcopy


def pprint(ar):
    for col in ar:
        print(col)
    print()


class SlicingFloorPlanTree(LinkedBinaryTree):
    class _Node(LinkedBinaryTree._Node):
        def __str__(self):
            try:
                print(self._element._element)
                print('error')
            except AttributeError as xd:
                pass
            return super.__str__(self)

    class Vertical(LinkedBinaryTree._Node):
        def __init__(self):
            self._dims = {'width': None, 'height': None}

        def __str__(self):
            return "Vertical Cut"

    class Horizontal(LinkedBinaryTree._Node):
        def __init__(self):
            self._dims = {'width': None, 'height': None}

        def __str__(self):
            return "Horizontal Cut"

    def __init__(self, token, left=None, right=None):

        super().__init__()
        self.counter = 0
        if left is None:
            if not isinstance(token, dict):
                raise ValueError("Token must be a a {height:x, width:x}")
            dimensions = token
            self._add_root(dimensions)
        else:
            raise Exception

    def _w(self, node, force=True):
        element = node._element
        if not isinstance(element, dict):
            dims = element._dims
        else:
            dims = element

        if force:
            if isinstance(element, self.Horizontal):
                dims['width'] = max(self._w(node._left), self._w(node._right))
            elif isinstance(element, self.Vertical):
                dims['width'] = self._w(node._left) + self._w(node._right)
        return dims['width']

    def _h(self, node, force=True):
        element = node._element
        if not isinstance(element, dict):
            dims = element._dims
        else:
            # its a cut
            dims = element

        if force:
            if isinstance(element, self.Horizontal):
                dims['height'] = self._h(node._left) + self._h(node._right)
            elif isinstance(element, self.Vertical):
                dims['height'] = max(self._h(node._left), self._h(node._right))
        return int(dims['height'])

    def cut_vertical(self, p):
        node = p._node
        dims = p.element()
        if self.is_leaf(p):
            node._element = self.Vertical()
            node._element.dims = dims
            left = self._add_left(p, deepcopy(dims))
            right = self._add_right(p, deepcopy(dims))
            return left, right
        else:
            raise Exception

    def cut_horizontal(self, p):
        node = p._node
        dims = p.element()
        if self.is_leaf(p):
            node._element = self.Horizontal()
            node._element._dims = dims
            left = self._add_left(p, deepcopy(dims))
            right = self._add_right(p, deepcopy(dims))
            return left, right
        else:
            raise Exception

    def compact(self):
        # Resize tree
        self._h(self._root)
        self._w(self._root)

    def draw(self):
        self.compact()
        width, height = self._w(self._root), self._h(self._root)
        my_map = [['.' for _ in range(width)] for _ in range(height)]
        self._draw(self.root(), (0, 0), my_map, True)
        for x in my_map:
            for y in x:
                print(y, end='')
            print()

    def _draw(self, p, offset, my_map, draw_self_border):
        print("Block nr:{} is {} x {} at offset".format(self.counter, self._w(p._node, False), self._h(p._node, False)),
              offset)

        self.counter += 1
        node = p._node._element
        w, h = offset
        draw_child_border = False
        if (self.left(p) and self.is_leaf(self.left(p))) == (self.right(p) and self.is_leaf(self.right(p))):
            draw_child_border = True
        else:
            draw_self_border = True
        for child in self.children(p):

            self._draw(child, (w, h), my_map, draw_child_border)
            if isinstance(node, self.Vertical):
                w += self._w(child._node)
            elif isinstance(node, self.Horizontal):
                h += self._h(child._node)

        w, h = offset
        width, height = self._w(p._node, False), self._h(p._node, False)
        # if self.is_leaf(p):

        print(w, h, width, height)
        print('creating rectangle {} x {}'.format(width, height))
        if True or draw_self_border:
            for col in range(width):
                #  x x x
                #  . . .
                #  . . .
                my_map[h][w + col] = '#'
            for col in range(width):
                #  . . .
                #  . . .
                #  x x x
                my_map[h + height - 1][w + col] = '#'
            for row in range(height):
                #  x . .
                #  x . .
                #  x . .
                my_map[h + row][w] = '#'
            for row in range(height):
                #  . . x
                #  . . x
                #  . . x
                my_map[h + row][w + width - 1] = '#'
                # if width == 19:
                #     pprint(my_map)

    def __str__(self):
        return self._intented_parenthetic(self.root(), 0)

    def _intented_parenthetic(self, p, ind=0):
        ans = ''
        ans += '  ' * ind + str(p.element()) + ' ' + str(self._w(p._node)) + ' x ' + str(self._h(p._node))
        if not self.is_leaf(p):
            ans += '(\n'
        else:
            ans += '\n'
        for child in self.children(p):
            ans += self._intented_parenthetic(child, ind + 1)
        if not self.is_leaf(p):
            ans += ' ' * ind + ')\n'
        return ans


def main():
    tree = SlicingFloorPlanTree(dict(height=4, width=4))

    left, right = tree.cut_horizontal(tree.root())
    left, right = tree.cut_vertical(left)

    left, right = tree.cut_vertical(left)
    left, right = tree.cut_vertical(left)
    left, right = tree.cut_horizontal(left)
    # #
    # tree.cut_horizontal(right)

    print(tree)
    tree.draw()


if __name__ == '__main__':
    main()
