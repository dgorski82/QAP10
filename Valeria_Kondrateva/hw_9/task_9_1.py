class Book:
    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False
        self.name_res = []


class User:
    def __init__(self, name):
        self.name = name
        self.book_list = []

    def take_book(self, book):
        assert book.reserved is False, 'Книгу читает другой пользователь'
        self.book_list.append(book)
        book.reserved = True

    def back_book(self, book):
        if book in self.book_list:
            book.reserved = False
            self.book_list.remove(book)

    @staticmethod
    def booking_book(book):
        assert book.reserved is False, 'Книга уже зарезервирована'
        book.reserved = True


book_a = Book('war and peace', 'L.Tolstoy', 1300, 556589222)
user_a = User('Lera')
user_b = User('Sasha')
user_a.take_book(book_a)
user_b.take_book(book_a)
