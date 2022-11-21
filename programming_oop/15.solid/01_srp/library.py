from books import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)

    def find_book(self, book_title: str):
        try:
            searched_book = next(filter(lambda b: b.title == book_title, self. books))

        except StopIteration:
            return f'Book {book_title} does not exist in your library!'

        return searched_book


book = Book('Ico', 'Penev', 'Plovdiv')
book.turn_page(3)
library = Library()
library.add_book(book)
print(library.find_book('Ico'))
