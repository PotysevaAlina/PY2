import doctest


class auto:
    def __init__(self, mark: str, serial: str, numer: str):
        """
        Создание и подготовка к работе объекта "Машина"
        :param mark: Марка машины
        :param serial: Серийный номер
        Примеры:
        >>> CAR = auto("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
        """
        if not isinstance(mark, str):
            raise TypeError("Напишите как текс")
        self.Mark = mark

        if not isinstance(serial, str):
            raise TypeError("Серийный номер это текст")
        self.Serial = serial

        self.Numer = None
        self.change_numer(numer)
        self.probeg = 0

    def __str__(self) -> str:
        """
        Функция которая создает строковое предстваление класс
        :return: str
        Примеры:
        >>> CAR = auto("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
        >>> CAR.__str__()
        """
        return f"Марка машины {self.mark}, Серийный Номер {self.serial} , Номер на авто {self.numer}"

    def __repr__(self)->str:
        """
                Функция которая позволяет копировать предстваление класса
                :return: str
                Примеры:
                >>> CAR = auto("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
                >>> CAR.__repr__()
                """
        a = self.__dict__
        a = str(a).replace(':','=').replace('{','').replace('}','').replace("_",'')
        b = a.split(',')
        c = ''
        for i,ii in enumerate(b):
             d = ii.replace("'",'',2)
             if i! = len(b)-1:
                 c = c + d + ','
             else:
                 c = c + d
        return f"{self.__class__.__name__}({c})"


    def change_numer(self, new_numer: str) -> None:
        """
            Смена номера в ГИБДД.
            :param new_numer: Ваш новый номер
            Примеры:
            >>> CAR = auto("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
            >>> CAR.change_numer('S010TY')
        """
        if not isinstance(new_numer, str):
            raise TypeError("Номер на машине это текст")
        if len(new_numer) == 5:
            raise ValueError("Номер состоит из 6 символов")
        self.Numer = new_numer

    @property
    def probeg(self):
        """
                Getter Пробег машины.
                    :param probeg: Ваш пробег
                    У стандартных машин пробег не известен
                    Примеры:
                    >>> CAR = auto("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
                """
        return self._probeg
    @probeg.setter
    def probeg(self, new_probeg):
        """
                        Setter Пробег машины.
                            :param new_probeg : Новый пробег
                            :param probeg: Ваш пробег
                            У стандартных машин пробег не известен
                            Примеры:
                            >>> CAR = auto("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
                        """
        self._probeg=new_probeg



class auto_from_USA(auto):
    """
           Создание и подготовка к работе объекта "Машина из Америки"
           :param Mark: Марка машины
           :param Serial: Серийный номер
           :param Numer: Номер на машине из неограниченого числа символо
           Отличие от класса машины в том что номер на машине может иметь произвольную длину!
           Примеры:
           >>> CAR = auto_from_USA("FORD", "S666-01", "GO8NO")  # инициализация экземпляра класса
           """
    def change_numer(self, new_numer)-> None:
        """
                   Переопределение метода смены номера"
                   :return None
                   Примеры:
                   >>> CAR = auto_from_USA("FORD", "S666-01", "GO8NO")  # инициализация экземпляра класса
                   """
        if not isinstance(new_numer, str):
            raise TypeError("Номер на машине это текст")
        self.Numer = new_numer

class auto_with_probeg(auto):
    def __init__(self, mark: str, serial: str, numer: str,probeg: int, cost : int):
        """
           Создание и подготовка к работе объекта "Машина с пробегом"
           :param mark: Марка машины
           :param serial: Серийный номер
           :param numer: Номер на машине из неограниченого числа символо
           :param probeg: Информация о пробеге машины
           :param cost : Цена в машине
           Отличие от класса машины в том что номер на машине может иметь параметр пробег!
           Примеры:
                    >>> CAR = auto_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)  # инициализация экземпляра класса
           """
        super().__init__(mark, serial, numer)
        self.probeg = probeg
        if not isinstance(cost, int):
            raise TypeError("Серийный номер это текст")
        self.cost = cost
    def iznos(self):
        """
                   Функция расчета износа машины
                   Примеры:
                            >>> CAR = auto_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)  # инициализация экземпляра класса
                            >>> CAR.iznos()
                   """
        cost=self.cost*(1/self.probeg)
        return cost
    def __str__(self):
        """
            Строковое представление перегружаю т.к. появился новый параметр
            Примеры:
                >>> CAR = auto_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)   # инициализация экземпляра класса
                >>> CAR.__str__()
        """
        return f"Марка машины {self.Mark}, Серийный Номер {self.Serial} , Номер на авто {self.Numer}, Количество пройденых киллометров {self.probeg}"

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

CAR = CAR = auto_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)
print(CAR.__str__())
print(CAR.__repr__())
