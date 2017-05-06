"""
Describe a recursive function for computing the nth Harmonic number,
Hn = ∑n
i=1 1/i.
"""

def harmonic(number):
    """
    Calculates /number/ harmonic number.
    
    :param number: harmonic numer to calculate 
    :return: value of that harmonic number
    """
    res = 1/number
    if number > 1:
        res += harmonic(number - 1)

    return res

if __name__ == '__main__':
    print(harmonic(3))