"""
Write a short recursive Python function that rearranges a sequence of integer
values so that all the even values appear before all the odd values.

i know that there are more optimal solutions but i quit like it
"""

def even_first(seq, start=0):
    if len(seq) == start+1:
        # no more numbers
        return []
    else:
        if seq[start] % 2 == 0:
            # if its even
            # add at beggining
            return [seq[start]] + even_first(seq, start + 1)
        else:
            # if its odd
            # add at end
            return even_first(seq, start + 1) + [seq[start]]

if __name__ == '__main__':
    data = list(range(10))
    print(even_first(data))