# Write a short Python function that counts the number of vowels in a given
# character string.

def count_vovels(word):
    vovels = 'aeiou'
    count = {}
    for letter in word.lower():
        if letter in vovels:
            count[letter] = count.get(letter, 0) + 1
    return count

if __name__ == '__main__':
    word = 'computer'
    print(count_vovels(word))