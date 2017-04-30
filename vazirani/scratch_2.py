

# for name in range(21, 41):
#     with open('R-3.{}'.format(name), 'w') as ff:
#         ff.write(' ')

MOD = 1000000007
def fast_power(base, power):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result

print (fast_power(2, 1))
# Output: 2
print( fast_power(2, 2))
# Output: 4
print (fast_power(2, 4))
# Output: 16
print (fast_power(3, 4))
# Output: 81
print (fast_power(2, 100))
# Output: 976371285