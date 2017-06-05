"""
Implement a class, SubstitutionCipher, with a constructor that takes a
string with the 26 uppercase letters in an arbitrary order and uses that for
the forward mapping for encryption (akin to the self. forward string in
our CaesarCipher class of Code Fragment 5.11). You should derive the
backward mapping from the forward version.
"""
from random import shuffle

class SubstitutionCipher():
    def __init__(self, key):
        self._forward = key
        self._backward = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, message):
        return self._transform(message, self._forward,  self._backward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward, self._forward)

    def _transform(self, original, code, template):
        print(code)
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = code.find(msg[k])
                msg[k] = template[j]
        return ''.join(msg)


if __name__ == '__main__':
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = list(key)
    shuffle(key)
    key = ''.join(key)
    # print(key)
    #############
    cipher = SubstitutionCipher(key)
    message = "ABCD"
    coded = cipher.encrypt(message)
    print('Secret:', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)