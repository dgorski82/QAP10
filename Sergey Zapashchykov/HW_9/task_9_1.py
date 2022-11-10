class Book:

    def __init__(self, title, author, pages, isbn, reserve=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserve = reserve


class User:

    def __init__(self, name):
        self.name = name
        self.user_book = []

    def reserve_book(self, book):
        if book.reserve is False:
            book.reserve = True

    def take_book(self, book):
        assert book not in self.user_book, f"{book} can't be taken."
        assert book.reserve is False, f"{book} can't be taken."
        self.user_book.append(book)

    def return_book(self, book):
        assert book in self.user_book, f"You didn't take {book}"
        self.user_book.remove(book)


book1 = Book('Hobbit', 'Tolkien', 314, '978-0-00-837-605-5')
book2 = Book('Fellowship of the Rings', 'Tolkien', 414, '984-0-00-548-546-1')

user1 = User('Anton')
user2 = User('Vlad')

user1.take_book(book1)
print(user1.user_book)

user1.return_book(book1)
print(user1.user_book)
user1.return_book(book1)

user2.reserve_book(book2)
user1.take_book(book2)
