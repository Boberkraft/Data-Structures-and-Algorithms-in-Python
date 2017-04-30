# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1

from array import array

def dot(aa, bb):
    cc = array('i')
    for i in range(len(aa)):
        cc.append(aa[i] * bb[i])
    return cc
    # dot production actualy return scalar
    # (singer number that is sum of all vector components)

if __name__ == '__main__':
    aa = array('i')
    bb = array('i')
    aa.fromlist([1,2,3,4,5])
    bb.fromlist([3,5,2,1,3])
    print(dot(aa,bb))