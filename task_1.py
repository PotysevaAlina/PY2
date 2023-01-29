class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = None
        self.__author = None
        self.__set_parametr(name,author)
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


    def __repr__(self):
        f = "Book"
        a = self.__dict__
        a = str(a).replace(':','=').replace('{','').replace('}','').replace("_",'').replace(f'{f}','')
        b = a.split(',')
        c = ''
        for i, ii in enumerate(b):
            d = ii.replace("'",'',2)
            if i != len(b) - 1:
                c = c + d+','
            else:
                c=c+d
        return f"{self.__class__.__name__}({c})"
    def __set_parametr (self, name, author):
        self.__name=name
        self.__author=author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        if not isinstance(pages, (int)):
            raise TypeError("Pages должно быть целым числом")
        self.pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Число страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name,author)
        if not isinstance(duration, (int, float)):
            raise TypeError("Duration должно быть целым числом")
        self.duration = duration

    def __str__(self):
        return f"Аудио книга {self._name}. Автор {self._author} . Длительность {self.duration}"
proverka=Book('book','is')
print(proverka.__repr__())
proverka= PaperBook('book','is',4)
print(proverka.__repr__())
proverka= AudioBook('book','is',2.43)
print(proverka.__repr__())
