"""
Python’s os module provides a function with signature walk(path) that
is a generator yielding the tuple (dirpath, dirnames, filenames) for each
subdirectory of the directory identified by string path, such that string
dirpath is the full path to the subdirectory, dirnames is a list of the names
of the subdirectories within dirpath, and filenames is a list of the names
of non-directory entries of dirpath. For example, when visiting the cs016
subdirectory of the file system shown in Figure 4.6, the walk would yield
( /user/rt/courses/cs016 , [ homeworks , programs ], [ grades ]).
Give your own implementation of such a walk function.
"""
import os

def my_walk(path):
    files = []
    dirs = []
    for file in os.listdir(path):
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            # if its a dir
            dirs.append(file)  # add to list
            # search that dir
            yield from my_walk(new_path)
        else:
            files.append(file)
    # every fille searched, yield what you got
    yield (path, dirs, files)

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, 'test.qml')
    for f in os.walk(path):
        print(f)
        print()
    print('*'*20)
    for f in my_walk(path):
        print(f)
        print()
