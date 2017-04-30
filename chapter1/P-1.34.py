# A common punishment for school children is to write out a sentence multiple
# times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.
from random import random, shuffle

def expand(words):
    new = {}
    for key, val in words.items():
        new[val] = key
    words.update(new)

def make_typo(sentence, letters):
    shuffle(letters)  # shuffle letters
    for a, b in letters:
        if a in sentence:
            # replace a with b
            return sentence.replace(a, b, 1)

if __name__ == '__main__':
    sentence = 'I will never spam my friends again'
    similar = dict(
        a='o',
        i='l',
        g='q',
        j='l',
        n='m',
        v='w')
    expand(similar)  # expand key items
    similar = list(similar.items())  # make it a list for shuffling
    prob = 80/1000
    for _ in range(1000):
        if random() < prob: # not 80 but shout be enought
            print(make_typo(sentence, similar))
        else:
            print(sentence)
