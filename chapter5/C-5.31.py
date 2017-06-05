"""
Describe a way to use recursion to add all the numbers in an n × n data
set, represented as a list of lists.
"""

def sum(data):
    if hasattr(data, "__iter__"):
        # if its iterable
        out = 0
        for el in data:
            # sum all its elements
            out += sum(el)
        return out
    else:
        return data



n = 5
# i know this is not the best way
data = [[1]*n]*n
print(data)
print(sum(data))