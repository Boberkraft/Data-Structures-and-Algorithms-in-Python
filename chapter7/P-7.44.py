"""
Write a simple text editor that stores and displays a string of characters
using the positional list ADT, together with a cursor object that highlights
a position in this string. A simple interface is to print the string and then
to use a second line of output to underline the position of the cursor. Your
editor should support the following operations:
• left: Move cursor left one character (do nothing if at beginning).
• right: Move cursor right one character (do nothing if at end).
• insert c: Insert the character c just after the cursor.
• delete: Delete the character just after the cursor (do nothing at end).

but what if there is only one character left?
What to do at the start of
"""

from PositionalList import PositionalList


class TextEditor:
    def __init__(self):
        self._data = PositionalList()
        self._data.add_first(None)
        self._cursor = self._data.first()
        self._size = 0

    def left(self):
        prev = self._data.before(self._cursor)
        if prev is not None:
            self._cursor = prev

    def right(self):
        nex = self._data.after(self._cursor)
        if nex is not None:
            self._cursor = nex

    def insert(self, char):
        self._size += 1
        self._data.add_after(self._cursor, char)
        self._cursor = self._data.after(self._cursor)

    def delete(self):
        nex = self._data.after(self._cursor)
        if nex is not None:
            self._data.delete(nex)
            self._size -= 1

    def __str__(self):
        end = ''
        node = self._data.first()

        for x in range(self._size + 1):
            if node == self._cursor:
                cursor = x
            node = self._data.after(node)
            if node is not None:
                end += node.element()
        end += '\n'
        end += ' ' * cursor + '^'
        return end


t = TextEditor()
t.insert('a')
t.insert('b')
t.insert('c')
t.insert('d')
t.insert('e')
print(t)
t.delete()
print(t)
