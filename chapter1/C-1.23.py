# Give an example of a Python code fragment that attempts to write an element
# to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

important_stuff = [0,0,0]

def exposed(index, num):
    important_stuff[index] = num

if __name__ == '__main__':
    x = 10
    try:
        exposed(x, 77)
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")
