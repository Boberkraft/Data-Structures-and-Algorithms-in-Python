# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def is_dinstinc(seq, many=5):
    cou = 0
    for num in seq:
        if num % 2 == 1:
            cou += 1
            if cou >= many:
                return True
        else:
            cou = 0
    return False

if __name__ == '__main__':
    data = [1,2,3,4,5,1,2,5,7,9]
    print(is_dinstinc(data))
