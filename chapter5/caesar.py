class CaesarCipher:
    def __init__(self, shift):
        self._forward = ''.join([chr(ord('A') + (num - ord('A') + shift)%26) for num in range(ord('A'), ord('Z') + 1)])
        self._backward = ''.join([chr(ord('A') + (num - ord('A') - shift)%26) for num in range(ord('A'), ord('Z') + 1)])
        print(self._forward)
        print(self._backward)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, oryginal, code):
        msg = list(oryginal)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "DUPA"
    coded = cipher.encrypt(message)
    print('Secret:', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)