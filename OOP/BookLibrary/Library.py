import Book

class Library:

    def __init__(self, books) -> None:
        self.books = books

    
    def set_active(self, book):
        self.active = book

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_book(self, book):
        for lib_book in self.books:
            if lib_book == book:
                return lib_book