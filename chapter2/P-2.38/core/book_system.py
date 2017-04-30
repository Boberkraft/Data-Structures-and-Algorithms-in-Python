"""Buying and viewing bought books"""
from file_manager import Files

class BookSystem:
    files = Files()
    last_shown = None

    def show_menu(self):
        print('Welcome in ebook.')
        print('1. Show all book')
        print('2. Show owned books')
        print('3. Show not owned books')
        print('4. But a book')
        print('5. Read a book')
        print('-'* 10)
        print('- For this menu type Menu.')
        print('- To buy a book type: 3 all_book_num')
        print('- To read a book type 5 owned_book_num')

    def read(self, num):
        owned = self.files.get_owend()
        book = owned[num-1]
        self.files.run_book(book)

    def but(self, num):
        all = self.files.get_books()
        owned = self.files.get_owend()
        to_buy = [book for book in all + owned if book not in owned]
        if to_buy[num-1] in owned:
            print('Book already owned')
            return
        self.files.add_book(to_buy[num-1])

    def show_all(self):
        print('You can buy fallowing books:')

        for index, book in enumerate(self.files.get_books()):
            print('{}: {}'.format(index+1, book))

    def show_not_owned(self):
        all = self.files.get_books()
        owned = self.files.get_owend()
        to_buy = [book for book in all+owned if book not in owned]
        self.last_shown = to_buy
        print('Not owned books:')
        for index, book in enumerate(to_buy):
            print('{}: {}'.format(index+1, book))

    def show_owned(self):
        owned = self.files.get_owend()
        print('Owned books:')

        for index, book in enumerate(self.files.get_owend()):
             print('{}: {}'.format(index+1, book))
        if not owned:
            print('No books owned')

    def buy_book(self, number):
        self.files.add_book(self.last_shown[number+1])

if __name__ == '__main__':
    book = BookSystem()
    book.show_all()
    print()
    book.show_not_owned()
    print()
    book.show_owned()