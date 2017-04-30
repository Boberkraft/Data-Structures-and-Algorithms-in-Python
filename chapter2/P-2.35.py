# Write a set of Python classes that can simulate an Internet application in
# which one party, Alice, is periodically creating a set of packets that she
# wants to send to Bob. An Internet process is continually checking if Alice
# has any packets to send, and if so, it delivers them to Bob’s computer, and
# Bob is periodically checking if his computer has a packet from Alice, and,
# if so, he reads and deletes it.
from time import time
from collections import defaultdict


class Internet:
    def __init__(self):
        self.queue = defaultdict(list)

    def send_msg(self, msg, where):
        self.queue[where].append(msg)

    def get_msg(self, who):
        msg = self.queue[who]
        if msg:
            del self.queue[who]
            return msg

class User:

    def __init__(self, name, internet, delay=1):
        self.name = name
        self.internet = internet
        self._last_action = 0
        self.delay = delay

    def can(self):
        if time() - self._last_action > self.delay:
            self._last_action = time()
            return True
        return False

    def send(self, msg, where):
        self.internet.send_msg(msg, where)

    def recive(self):
        msg = self.internet.get_msg(self.name)
        if msg:
            print('{} got {}'.format(self.name, msg))
            del msg  # no need to delete but why not

if __name__ == '__main__':
    internet = Internet()
    alice = User('Alice', internet, 1)
    bob = User('Bob', internet, 2)

    while True:
        if bob.can():
            bob.recive()

        if alice.can():
            alice.send('I LOVE YOU <3', 'Bob')
