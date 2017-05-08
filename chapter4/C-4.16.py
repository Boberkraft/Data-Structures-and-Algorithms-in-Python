"""
Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be snap&stop .

Why not to create a some new string objects every call?
Dont wanted to do it with list
"""


def reverse(word):
    """Reversed middle"""
    if len(word)//2 > 1:
        midle = word[1:-1]
        # change first and last
        # reverse middle
        word = word[-1] + reverse(midle) + word[0]
    return word


if __name__ == '__main__':
    word = '12345678'
    print(reverse(word))