"""
Redesign the CaesarCipher class as a subclass of the SubstitutionCipher
from the previous problem.
"""
from substitutioncisper import SubstitutionCipher


class CaesarCisper(SubstitutionCipher):
    def __init__(self, shift):
        self._backward = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._forward = ''.join([self._backward[(i-shift) % len(self._backward)]for i in range(len(self._backward))])

if __name__ == '__main__':
    cipher = CaesarCisper(3)
    message = 'DUPA'
    coded = cipher.encrypt(message)
    print(coded)
    decrypt = cipher.decrypt(coded)
    print(decrypt)