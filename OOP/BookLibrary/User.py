from Library import Library
from Page import Page
from Book import Book

class User:

    def __init__(self, username, library) -> None:
        self.username = username
        self.library = library
        self.active = None

    
    def read(self, book):
        self.active = self.library.get_book(book)
        print(self.active.get_current_page()) 

    
    def next_page(self):
        print(self.active.next_page())

    
    def prev_page(self):
        print(self.active.prev_page())
    

p1 = Page("Ciao come stai, questa è la p1")
p2 = Page("Ciao come stai, questa è la p2")
p3 = Page("Ciao come stai, questa è la p3")


b1 = Book("Come stai", [p1, p2, p3])

p1 = Page("Che st  ronzo, p1")
p2 = Page("Che stronzo, p2")

b2 = Book("Stronzo", [p1, p2])


l1 = Library([b1, b2])

u1 = User("Gino", l1)


u1.read(b1)

u1.next_page()
u1.next_page()
u1.next_page()