"""
Describe a recursive algorithm for finding the maximum element in a sequence,
S, of n elements. What is your running time and space usage?

"""


def find_max(data, highest=0):
    """
    Speed: O(n)
    Space: O(n)
    """
    if data[0] > highest:
        highest = data[0]
    if len(data) > 1:
        return find_max(data[1:], highest)
    else:
        return highest

if __name__ == '__main__':
    data = [1,2,3,60,1,2]
    print(find_max(data))