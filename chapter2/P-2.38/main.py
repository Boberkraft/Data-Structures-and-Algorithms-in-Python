# Write a Python program that simulates a system that supports the functions
# of an e-book reader. You should include methods for users of your
# system to “buy” new books, view their list of purchased books, and read
# their purchased books. Your system should use actual books, which have
# expired copyrights and are available on the Internet, to populate your set
# of available books for users of your system to “purchase” and read.


import sys
sys.path.append('core')
from book_system import BookSystem

commands = {'1'}
if __name__ == '__main__':
    books = BookSystem()
    books.show_menu()
    while True:
        print()
        user = input(">> ")
        if user in {'Menu', 'menu'}:
            books.show_menu()
        elif user == '1':
            books.show_all()
        elif user == '2':
            books.show_owned()
        elif user == '3':
            books.show_not_owned()
        elif user[0] == '4':
            try:
                number, book = user.split()
                books.but(int(book))
            except ValueError:
                books.show_not_owned()
        elif user[0] == '5':
            try:
                number, book = user.split()
                books.read(int(book))
            except ValueError:
                books.show_owned()
