class Book:
    def __init__(self, book_name: str, author: str, pages_amount: int, isbn: str, genre: list, reserved_book: bool):
        self.book_name = book_name
        self.author = author
        self.pages_amount = pages_amount
        self.isbn = isbn
        self.genre = genre
        self.reserved_book = reserved_book


class Reader:
    def __init__(self, reader_name):
        self.reader_name = reader_name
        self.taken_reader_books = list()
        self.reserved_reader_books = list()

    def take_book(self, book):
        assert book.reserved_book is False, f"{book.book_name} book was taken or reserved by another reader"
        self.taken_reader_books.append(book.book_name)
        book.reserved_book = True
        print(f"{self.reader_name} took books: {', '.join(self.taken_reader_books)}")

    def reserve_book(self, book):
        assert book.reserved_book is False, f"{book.book_name} book was taken or reserved by another reader"
        self.reserved_reader_books.append(book.book_name)
        book.reserved_book = True
        print(f"{self.reader_name} reserved books: {', '.join(self.reserved_reader_books)}")

    def return_book(self, book):
        assert book.reserved_book is True, f"{book.book_name} book was not taken or reserved by another reader"
        if book.reserved_book is True and book.book_name in self.taken_reader_books:
            self.taken_reader_books.remove(book.book_name)
            print(f"{book.book_name} was returned to the library")
        elif book.reserved_book is True and book.book_name in self.reserved_reader_books:
            self.reserved_reader_books.remove(book.book_name)
            print(f"{book.book_name} book was returned to the library")
        book.reserved_book = False


alice_in_wonderland = Book("Alice's adventures in Wonderland", "Lewis Carroll",
                           48, "978-5-17-144783-0", ["fantasy", "literary nonsense"], False)

three_comrades = Book("Three Comrades", "Erich Maria Remarque", 384, "978-5-17-086280-1", ["War novel"], False)

alesia = Reader("Alesia")
kate = Reader("Kate")

alesia.take_book(alice_in_wonderland)
alesia.take_book(three_comrades)
alesia.return_book(alice_in_wonderland)
alesia.return_book(three_comrades)
kate.take_book(alice_in_wonderland)
kate.reserve_book(three_comrades)
kate.return_book(three_comrades)
alesia.take_book(three_comrades)
