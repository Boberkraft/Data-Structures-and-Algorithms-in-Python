"""
Describe a recursive function for converting a string of digits into the integer
it represents. For example, 13531 represents the integer 13,531.
"""

ints = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,' 8':8,'9':9}
def to_int(digits, mult=0):
    if len(digits) > 0:
        res = ints[digits[-1]] * 10**mult
        res += to_int(digits[:-1], mult+1)
        return res
    else:
        # no more digits
        return 0
if __name__ == '__main__':
    print(to_int('1345'))