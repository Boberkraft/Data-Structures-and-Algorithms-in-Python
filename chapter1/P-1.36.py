# Write a Python program that inputs a list of words, separated by whitespace,
# and outputs how many times each word appears in the list. You
# need not worry about efficiency at this point, however, as this topic is
# something that will be addressed later in this book.

if __name__ == '__main__':
    words = input('words: ')
    count = {}
    for word in words.split():
        count[word] = count.get(word, 0) + 1
    print(count)