"""
Write a program that can perform the Caesar cipher for English messages
that include both upper- and lowercase characters.
"""

from caesar import CaesarCipher

class NewCaesar(CaesarCipher):
    def _transform(self, oryginal, code):
        msg = list(oryginal)
        for k in range(len(msg)):
            if msg[k].isalpha():
                up = msg[k].isupper()
                j = ord(msg[k].upper()) - ord('A')
                msg[k] = code[j] if up else code[j].lower()
        return ''.join(msg)

if __name__ == '__main__':
    cipher = NewCaesar(3)
    message = "Hello How are you!"
    coded = cipher.encrypt(message)
    print('Secret:', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)