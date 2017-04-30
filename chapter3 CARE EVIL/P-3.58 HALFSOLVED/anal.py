"""
the reasult may exeed 1min because computers are not perfect and math can sometimes take longer
# bro where is unique3? In chapter 4? nooo to mee


i have a MemoryError with unique2 near 60s :P
if someone have method how to make this pm me please :)
andrzej.bisewski@gmail.com 

Traceback (most recent call last):
  File "C:/Users/Bobi/PycharmProjects/newex/newbookalgry/chapter3 CARE EVIL/P-3.58/anal.py", line 58, in <module>
    elapsed = analize(f, data)
  File "C:/Users/Bobi/PycharmProjects/newex/newbookalgry/chapter3 CARE EVIL/P-3.58/anal.py", line 29, in analize
    f(data)
  File "C:\Users\Bobi\PycharmProjects\newex\newbookalgry\chapter3 CARE EVIL\P-3.58\unique.py", line 32, in unique2
    temp = sorted(S)                # create a sorted copy of S
MemoryError

"""
from unique import *
from time import time

class FakeList:
    def __init__(self, len):
        self.counter = 1
        self.__len__ = len

    def __getitem__(self, item):
        if item >= self.__len__:
            raise StopIteration()
        else:
            self.counter += 1
        return self.counter


    def __setitem__(self, key, value):
        pass


savings = 0
def analize(f, data):
    start = time()
    f(data)
    return time() - start

def save(name, data_size, time):
    global savings
    savings += 1
    with open('result', 'a') as f:
        f.write('{} needs {:.4f} s for n about {}\n'.format(name, time, data_size))

def check(f, data):
    print(data-1, analize(f, list(range(data-1))))
    print(data, analize(f,list(range(data))))
    print(data+1, analize(f,list(range(data+1))))

functions = [unique2]



if __name__ == '__main__':

    for f in functions:

        bottom = 0
        top = 101
        wiggled = False
        while True:
            n = (top - bottom) // 2
            bet = bottom + n
            data = FakeList(bet)
            elapsed = analize(f, data)
            print(bet, elapsed)
            if top - bottom in range(0, 100):
                save(f.__name__, bet, analize(f, list(range(bet - 1))))
                print('WHOHOH'*10)
                print('for n =', n)
                save(f.__name__, bet, elapsed)
                break
            if elapsed > 60:
                    # to high
                top = bet
                if not wiggled:
                    wiggled = True
            else:
                bottom = bet
                if not wiggled:
                    # to low
                    top = 2*top






