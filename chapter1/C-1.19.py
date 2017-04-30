# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

def generate(start, end):
    return [chr(num) for num in range(ord(start), ord(end)+1)]

if __name__ == '__main__':
    print(generate('a', 'z'))
