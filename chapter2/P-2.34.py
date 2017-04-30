# Write a Python program that inputs a document and then outputs a barchart
# plot of the frequencies of each alphabet character that appears in
# that document.
from collections import Counter


def charplot(data):
    for char, times in data.items():
        if not char.isspace():
            print('[{}]:{}'.format(char, 'x'*times))

if __name__ == '__main__':
    # path = input('Path:')
    path = 'characters'
    with open(path) as ff:
        x = Counter(ff.read())
    charplot(x)