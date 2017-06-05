"""
Write a Python function that takes two three-dimensional numeric data
sets and adds them componentwise.
"""

def add(data1, data2):
    if hasattr(data1, '__iter__'):
        out = []
        for i in range(len(data1)):
            out.append(add(data1[i], data2[i]))
        return out
    else:
        return data1 + data2

if __name__ == '__main__':
    data1 = [[1 for _ in range(5)] for _ in range(5)]
    data2 = [[i for i in range(5)] for _ in range(5)]
    print(data1)
    print(add(data1, data2))