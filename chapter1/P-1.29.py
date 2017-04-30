# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

def generate(word, letters):
    if len(letters) == 0:
        yield word
    else:
        for letter in letters:
            for val in generate(word+letter, letters.replace(letter, '')):
                yield val


if __name__ == '__main__':
    for seq in generate('', 'catdog'):
        print(seq)

