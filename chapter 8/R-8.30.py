"""
The build expression tree method of the ExpressionTree class requires
input that is an iterable of string tokens. We used a convenient example,
(((3+1)x4)/((9-5)+2)) , in which each character is its own token,
so that the string itself sufficed as input to build expression tree.
In general, a string, such as (35 + 14) , must be explicitly tokenized
into list [ ( , 35 , + , 14 , ) ] so as to ignore whitespace and to
recognize multidigit numbers as a single token. Write a utility method,
tokenize(raw), that returns such a list of tokens for a raw string.

Or i can user regular expression as the help states


"""
import re

def tokenize(raw):
    tokens = 'x+*-/()'
    stack = []
    token = ''
    for char in raw:
        if char in tokens:
            if len(token) > 0:
                stack.append(token)
                token = ''
            stack.append(char)
            continue
        elif char != ' ':
            #its a number
            token += char
    return stack

def tokenize1(raw):
    regex = r"[0-9]+|\(|\)|[-/+*x]"

    matches = re.finditer(regex, raw)
    return [match.group() for match in matches]

print(tokenize('(35+14)'))
print(tokenize1('(35+14)'))