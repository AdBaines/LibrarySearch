class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.books = []

    def __repr__(self):
        return f'{self.name}-{self.age}'

    def display_books(self):
        if self.books:
            print(f"Books by {self.name}:")
            for book in self.books:
                print(f"- {book.title} ({book.year})")
        else:
            print(f"No books found for {self.name}")

class Book:
    def __init__(self, title, year, authors=None):
        self.title = title
        self.year = year
        if authors is None:
            self.authors = []
        else:
            self.authors = authors

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, new_authors):
        for a in new_authors:
            if not isinstance(a, Author):
                raise TypeError
            else:
                a.books.append(self)
        self._authors = new_authors

    def __repr__(self):
        return f'{self.title}-{self.year}'



## Main Program ##
auth1 = Author('George R. R. Martin', 74)
auth2 = Author('Anthony Reynolds', 30)
auth3 = Author('Jesus Christ', 21)  

b1 = Book('A Game of Thrones', 1996, [auth1])
b2 = Book('The Ruination', 2022, [auth2])
b3 = Book('The Bible', 1, [auth3])

auth1.display_books()
print('_______________')
auth2.display_books()
print('_______________')
auth3.display_books()