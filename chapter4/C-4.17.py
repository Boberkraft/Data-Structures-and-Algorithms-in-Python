"""
Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, racecar and
gohangasalamiimalasagnahog are palindromes.
"""

def is_palindrome(word):
    """Returns if word is palindrome"""
    if len(word) > 2:
        if word[0] == word[-1]:
            # if first and last are the same
            # check if others are the same
            return is_palindrome(word[1:-1])
        else:
            # its not the same
            return False
    else:
        return True

if __name__ == '__main__':
    word1 = 'radar'
    word2 = 'gohangasalamiimalasagnahog'
    word3 = 'racecar'
    word4 = 'ra3ecar'
    print(is_palindrome(word1))
    print(is_palindrome(word2))
    print(is_palindrome(word3))
    print(is_palindrome(word4))
    print(is_palindrome(''))