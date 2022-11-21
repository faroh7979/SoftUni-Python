class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f'Book {self.title} with author {self.author} is on page {self.page}'
