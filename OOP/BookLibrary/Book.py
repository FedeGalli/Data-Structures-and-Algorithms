import Page

class Book:

    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages
        self.isActive = False
        self.current_page = 0

        
    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
        
        return self.pages[self.current_page].content

    
    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        
        return self.pages[self.current_page].content
    

    def get_current_page(self):
        return self.pages[self.current_page].content