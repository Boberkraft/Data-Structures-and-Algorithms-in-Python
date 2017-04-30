# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

def read():
    data = []
    try:
        while True:
            data.append(input())
    except EOFError as ee:
        pass
    return data


if __name__ == '__main__':

    data = read()
    print(data[::-1])