class Book:
    Name: str
    Author: str
    PagesCount: int
    ISBN: str

    def __init__(self, name: str, author: str, pages_count: int, isbn: str):
        self.Name = name
        self.Author = author
        self.PagesCount = pages_count
        self.ISBN = isbn

    def __eq__(self, other):
        if type(other) == str:
            return self.ISBN == other
        elif type(other) == Book:
            return self.ISBN == other.ISBN
        else:
            return False

    def __str__(self):
        return f'Name: {self.Name}, Author: {self.Author}, Pages: {self.PagesCount}, ISBN: {self.ISBN}'


class Library:
    Books: dict[str, Book] = {}
    ReservationList: dict[str, str] = {}

    def add_book(self, book: Book):
        if book.ISBN not in self.Books:
            self.Books.update({book.ISBN: book})

    def __deliver_book(self, book_to_deliver: Book) -> Book:
        del self.Books[book_to_deliver.ISBN]
        if book_to_deliver.ISBN in self.ReservationList.keys():
            del self.ReservationList[book_to_deliver.ISBN]

        return book_to_deliver

    def get_book(self, person_name: str, isbn: str) -> Book:
        if isbn in self.Books.keys():
            if isbn in self.ReservationList.keys():
                if self.ReservationList[isbn] == person_name:
                    print(f'{person_name} took the {isbn}')
                    return self.__deliver_book(self.Books[isbn])
                else:
                    print(f'{person_name} can not take the book')
            else:
                print(f'{person_name} took the {isbn}')
                return self.__deliver_book(self.Books[isbn])

    def reserve_book(self, person_name: str, isbn: str) -> bool:
        reservation_result = False
        if isbn in self.Books:
            if isbn not in self.ReservationList.keys():
                reservation_result = True
                self.ReservationList.update({isbn: person_name})
                print(f'{person_name} has reserved the {isbn}')
            else:
                print(f'{person_name} has not reserved the {isbn}')

        return reservation_result

    def return_book(self, book_to_return: Book) -> bool:
        if book_to_return is None:
            return False

        return_result = False
        if book_to_return.ISBN not in self.Books.keys():
            self.Books.update({book_to_return.ISBN: book_to_return})
            return_result = True
            print('Book returned')
        else:
            print('Book can not be returned')

        return return_result

    def cancel_reservation(self, person_name: str, isbn: str) -> bool:
        cancel_result = False
        if isbn in self.Books.keys():
            if isbn in self.ReservationList.keys():
                if self.ReservationList[isbn] == person_name:
                    del self.ReservationList[isbn]
                    cancel_result = True
                    print(f'{person_name} canceled reservation {isbn}')
            else:
                print(f'{isbn} not reserved')
        else:
            print(f'{isbn} is not exist')

        return cancel_result


class Person:
    Name: str
    Books: list[Book] = []
    library: Library

    def __init__(self, name: str, lib: Library):
        self.Name = name
        self.library = lib

    def __str__(self):
        return f'Person: {self.Name}'

    def get_book(self, isbn: str):
        book = library.get_book(self.Name, isbn)
        if book is not None:
            self.Books.append(book)

    def return_book(self, book_to_return: Book) -> bool:
        result = library.return_book(book_to_return)
        if result:
            self.Books.remove(book_to_return)

        return result

    def reserve_book(self, isbn: str) -> bool:
        return library.reserve_book(self.Name, isbn)

    def cancel_reservation(self, isbn) -> bool:
        return library.cancel_reservation(self.Name, isbn)


library = Library()

library.add_book(Book("Name1", "Author1", 132, "Book1"))
library.add_book(Book("Name2", "Author2", 123, "Book2"))
library.add_book(Book("Name3", "Author3", 321, "Book3"))

p1 = Person("Robby Williams", library)
p2 = Person("Kiano Rives", library)

p1.reserve_book("Book1")
p2.reserve_book("Book2")

p2.get_book("Book2")
p1.return_book(p1.Books[0])

p2.get_book("Book1")
p2.cancel_reservation("Book4")
