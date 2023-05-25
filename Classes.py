class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.books = []

    def __repr__(self):
        return f'{self.name}-{self.age}'

class Book:
    def __init__(self, title, year, authors=None):
        self.title = title
        self.year = year
        if authors is None:
            self.authors = []
        else:
            self.authors = authors

    def set_authors(self, new_authors):
        for a in new_authors:
            if not isinstance(a, Author):
                raise TypeError
            else:
                a.books.append(self)
        self.authors = new_authors

    def __repr__(self):
        return f'{self.title}-{self.year}'


## Main Program ##
auth1 = Author('George R. R. Martin', 74)
auth2 = Author('Anthony Reynolds', 30)
auth3 = Author('Jesus Christ', 21)
print(f'{auth1}={auth1.books}')
print(f'{auth2}={auth2.books}')
print(f'{auth3}={auth3.books}')
b1 = Book('A Game of Thrones', 1996, [auth1])
b2 = Book('The Ruination', 2022, [auth2])
print('_______________')

print('_______________')
print(b1.authors)
print(b2.authors)
