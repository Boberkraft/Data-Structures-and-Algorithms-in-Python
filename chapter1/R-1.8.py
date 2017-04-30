# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

if __name__ == '__main__':

    s = 'computer'
    n = len(s)

    for k in range(-n, 0):
        print(s[k])
        j = n + k
        print(s[j])
