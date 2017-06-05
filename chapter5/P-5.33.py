"""
Write a Python program for a matrix class that can add and multiply twodimensional
arrays of numbers, assuming the dimensions agree appropriately
for the operation

I just implemented is basing on tip.
"""

def add(data1, data2):
    if hasattr(data1, '__iter__'):
        out = []
        for i in range(len(data1)):
            out.append(add(data1[i], data2[i]))
        return out
    else:
        return data1 + data2

def multiply(data1, data2):
    out = [[None] * len(data1[1]) for _ in range(len(data1))]
    for i in range(len(data1)):
        for j in range(len(data2)):
            ans = sum([data1[i][x]*data2[x][j] for x in range(len(data1[0]))])
            out[i][j] = ans
    return out

if __name__ == '__main__':
    data1 = [[1 for _ in range(5)] for _ in range(5)]
    data2 = [[i for i in range(5)] for _ in range(5)]
    print(data1)
    print(add(data1, data2))
    print(multiply(data1, data2))