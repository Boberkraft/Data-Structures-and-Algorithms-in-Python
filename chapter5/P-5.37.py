"""
Design a RandomCipher class as a subclass of the SubstitutionCipher
from Exercise P-5.35, so that each instance of the class relies on a random
permutation of letters for its mapping.
"""
from substitutioncisper import SubstitutionCipher


class RandomCisper(SubstitutionCipher):
    def __init__(self):
        from random import shuffle
        self._backward = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rand = list(self._backward)
        shuffle(rand)
        self._forward = ''.join(rand)