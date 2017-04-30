# Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible
# order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function

from random import randint

def shuffle(data):
    for index in range(len(data)):
        ran = randint(0, len(data)-1)
        data[index], data[ran] = data[ran], data[index]


if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9,10]
    shuffle(data)
    print(data)

