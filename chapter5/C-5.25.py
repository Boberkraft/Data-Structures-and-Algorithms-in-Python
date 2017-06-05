"""
The syntax data.remove(value) for Python list data removes only the first
occurrence of element value from the list. Give an implementation of a
function, with signature remove all(data, value), that removes all occurrences
of value from the given list, such that the worst-case running time
of the function is O(n) on a list with n elements. Not that it is not efficient
enough in general to rely on repeated calls to remove
"""

def remove_all(data, value):
    shift = 0
    i = 0
    while True:
        # if el is value, place el + shift in that place
        # (if  el + shift is value, value +=1) till index error.
        if data[i+shift] == value:
            shift += 1
        else:
            data[i] = data[i + shift]
            i += 1
        if i + shift >= len(data):
            # everything shifted. Now delete trash at the end
            for _ in range(shift):
                data.pop()
            return



if __name__ == '__main__':
    data = [1,2,3,1,4,2] # [2,3,4,2]
    remove_all(data, 1)
    print(data)