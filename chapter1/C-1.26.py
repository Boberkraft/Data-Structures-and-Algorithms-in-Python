# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example,
# if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

if __name__ == '__main__':

    a, b, c = map(int, input('Please enter 3 integers: a b c: ').split())
    if a + b == c:
        print('a + b = c')
    elif b - c == a:
        print('a = b - c')
    elif a * b == c:
        print('a * b = c')