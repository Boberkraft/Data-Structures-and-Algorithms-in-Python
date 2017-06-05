class SubstitutionCipher:
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
