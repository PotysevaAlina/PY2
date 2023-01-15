BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
# TODO написать класс Book
class Book():
    def __init__(self, id_, name, pages):
        self.id_=id_
        self.name=name
        self.pages=pages
    def get_id_(self):
        return (self.id_)




# TODO написать класс Library

class Library():

    def __init__(self, books=None):
        self.type_error=type(None)
        if books==None:
            self.books=[0]
            self.books[0]=None

        else:
            self.books=books


    def get_next_book_id(self):
        if type(self.books[0])==self.type_error:
            self.count_id_=1
        else:
            for n, i in enumerate(self.books):
                self.count_id_=i.get_id_()+1

        return (self.count_id_)

    def get_index_by_book_id(self, index_id):
        key=None

        for n,i in enumerate(self.books):
            try:
                if i.get_id_()==index_id:
                    key=n
                    break
                else:
                    raise ValueError
            except ValueError:
                key='ValueError:"Книги с запрашиваемым id не существует"'
        return(key)


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1