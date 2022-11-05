class Book:

    def __init__(self, name: str, author: str, pages: int, isbn: int, reserved=False):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


class Visitor:

    def __init__(self, visitor_name: str):
        self.visitor_name = visitor_name
        self.taken_lst = list()

    def get_book(self, book):
        assert book not in self.taken_lst, print(f'{self.visitor_name} {book.name} и так уже у тебя')
        assert book.reserved is False, print(f'{self.visitor_name} не может взять {book.name}')
        self.taken_lst.append(book)
        book.reserved = True

    def reserve_book(self, book):
        assert book.reserved is False, print(f'{self.visitor_name} не может зарезервировать {book.name}')
        book.reserved = True

    def return_book(self, book):
        assert book in self.taken_lst, print(f'{self.visitor_name} не может вернуть {book.name}')
        self.taken_lst.remove(book)
        book.reserved = False


book_1 = Book('Книга_1', 'Автор_1', 555, 55555)
book_2 = Book('Книга_2', 'Автор_2', 666, 77777)

v1 = Visitor('Посетитель_1')
v2 = Visitor('Посетитель_2')

print(v1.get_book(book_1))
print(v1.get_book(book_1))

print(v2.get_book(book_1))
print(v2.reserve_book(book_2))
print(v1.get_book(book_2))

print(v1.return_book(book_1))
print(v2.get_book(book_1))
