# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example,
# if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

def remove_punc(sentance):
    punc = [',', '.', "'", '"']
    for el in punc:
        sentance = sentance.replace(el, '')
    return sentance

if __name__ == '__main__':
    test = """Let's try, Mike."""
    print(remove_punc(test))
