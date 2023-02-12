import doctest

class PLANTS:
    def __init__(self, Type: str, Name: str, Latin_name: str):
        """
        Создание и подготовка к работе объекта "Растение"
        :param Type: Тип растения
        :param Name: Название
        :param latin_name: Латинское название
        Примеры:
        >>> PLANT = PLANTS("Tree", "Spruse", 'Picea') #инициализация экземпляра класса
        """

        if not isinstance(Type, str):
            raise TypeError("Должен быть текст")
        self.Type = Type

        if not isinstance(Name, str):
            raise TypeError("Должен быть текст")
        self.Name = Name

        if not isinstance(Latin_name, str):
            raise TypeError("Должен быть текст")
        self.Latin_name = Latin_name


    def __str__(self)-> str:
        """
        Функция которая создает строковое предстваление класс
        :return: str
        Примеры:
        >>> PLANT = PLANTS("Tree", "Spruse", 'Picea')  # инициализация экземпляра класса
        >>> PLANT.__str__()
        """
        return f"Тип растения {self.Type}, Название {self.Name} , Название на латыни {self.Latin_name}"

    def __repr__(self)->str:
        """
                Функция которая позволяет копировать предстваление класса
                :return: str
                Примеры:
                >>> PLANT = PLANTS("Tree", "Spruse", 'Picea')   # инициализация экземпляра класса
                >>> PLANT.__repr__()
                """

        a = self.__dict__
        a = str(a).replace(':','=').replace('{','').replace('}','').replace("_",'')
        b = a.split(',')
        c = ''
        for i, ii in enumerate(b):
             d = ii.replace("'",'',2)
             if i != len(b) - 1:
                 c = c + d + ','
             else:
                 c = c + d
        return f"{self.__class__.__name__}({c})"


    def change_name(self, new_name: str) -> None:
        """
        Смена название
        :param new_name: Новое название растения
        Примеры:
        >>> PLANT = PLANTS("Tree", "Spruse", 'Picea')
        >>> PLANT.change_name('Pine')
        """

        if not isinstance(new_name, str):
            raise TypeError("Должен быть текст")
        self.Name = new_name


    def change_latin_name(self, new_latin_name: str) -> None:
        """
        Смена латинского названия
        :param new_latin_name: Новое название на латыни
        Примеры:
        >>> PLANT = PLANTS("Tree", "Spruse", 'Picea')
        >>> PLANT.change_latin_name('Pinus')

        """
        if not isinstance(new_latin_name, str):
            raise TypeError("Должен быть текст")
        self.Latin_name = new_latin_name

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации