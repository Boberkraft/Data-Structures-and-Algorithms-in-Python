"""Class for dealing with opening files and getting available books

    Only works on windows :)
"""
import os


class Files:
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = self.program_path()
        self.book_path = self.path + '\\books\\'

    def add_book(self, name):
        """Add book to purchased ones"""
        with open(self.book_path+'owned', 'a') as ff:
            ff.write(name+'\n')

    def get_books(self):
        with open(self.book_path+'available') as ff:
            return [line.strip() for line in ff.read().split('\n') if line]

    def get_owend(self):
        with open(self.book_path+'owned') as ff:
            return [line.strip() for line in ff.read().split('\n') if line]

    @staticmethod
    def program_path():
        path = os.getcwd()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir('..')
        new_path = os.getcwd()
        os.chdir(path)
        return new_path

    def run_book(self, name):
        os.startfile('{}{}.pdf'.format(self.book_path, name))

print(str())
if __name__ == '__main__':
    print('Current working directory:')
    print(Files.program_path())
    files = Files()
    # files.run_book('Answers for book')
    print(files.get_owend())
    print(files.get_books())

