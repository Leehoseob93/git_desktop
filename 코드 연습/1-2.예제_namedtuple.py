from collections import namedtuple
Book = namedtuple('Book',['title','author','year'])
book1 = Book('1984','george Orwell','1949')
book2 = Book('To Kill a Mockingbird','Harper Lee','1960')

print(f'{book1.title}')