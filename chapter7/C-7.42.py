"""
Write a Scoreboard class that maintains the top 10 scores for a game application
using a singly linked list, rather than the array that was used in
Section 5.5.1.
"""


class Scoreboard:
    class _Note:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.header = self._Note(None, None)
        self.size = -1

    def add(self, entry):
        self.size += 1
        node = self.header
        if self.size == 0:
            self.header.next = self._Note(entry, None)
        else:
            prev = self.header
            node = self.header.next
            while True:

                if node is None or node.element < entry:
                    prev.next = self._Note(entry, node)
                    return
                print('ok')
                prev, node = node, node.next

    def __getitem__(self, item):
        if item >= self.size + 1:
            raise IndexError
        else:
            node = self.header.next
            for _ in range(item):
                node = node.next
            return node.element

    def __len__(self):
        return self.size

    def __str__(self):
        return "[{}]".format(', '.join([str(node) for node in self]))


score = Scoreboard()
score.add(1)
score.add(3)
score.add(2)

print(score)
