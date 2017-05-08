"""
Implement a recursive function with signature find(path, filename) that
reports all entries of the file system rooted at the given path having the
given file name.
"""
import os

def find(path, filaname):
    if os.path.isdir(path):
        for file in os.listdir(path):
            # for file in directory
            if file == filaname:
                # if file with serching name have been found
                yield os.path.join(path, filaname)  # yield it
            new_path = os.path.join(path, file)
            yield from find(new_path, filaname)

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    filaname = 'bird'
    for file in find(path, filaname):
        print(file)
