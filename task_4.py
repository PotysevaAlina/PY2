import doctest

class Auto:
    def __init__(self, car_brand: str, serial_number: str, number: str):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param car_brand: Марка автомобиля
        :param serial_number: Серийный номер
        :param number: Номер автомобиля
        Примеры:
        >>> Auto = Auto("FORD", "S666-01", "G088NO")
        """
        if not isinstance(car_brand, str):
            raise TypeError("Марка автомобиля должна быть текстом")
        self.car_brand = car_brand

        if not isinstance(serial_number, str):
            raise TypeError("Серийный номер автомобиля должен быть текстом")
        self.serial_number = serial_number

        if not isinstance(number, str):
            raise TypeError("Номер автомобиля должен быть текстом")
        self.number = serial_number

    def __str__(self) -> str:
        """
        Функция, которая создает строковое представление класса
        :return: str
        Примеры:
        >>> Auto = Auto("FORD", "S066-01", "GO88NO")
        >>> Auto.__str__()
        """
        return f"Марка автомобиля {self.car_brand}, Серийный номер автомобиля {self.serial_number}, " \
               f"Номер автомобиля {self.serial_number}"

    def change_number(self, new_number: str) -> None:
        """
        Смена номера автомобиля
        :param new_number: Новый номер автомобиля
        Примеры:
        >>> Auto = Auto("FORD", "S666-01", "GO88NO")
        >>> Auto.change_number("S010TY")
        """
        if not isinstance(new_number, str):
            raise TypeError("Номер автомобиля должен быть текстом")
        if len(new_number) != 6:
            raise ValueError("Номер автомобиля должен состоять из 6 символов")
        self.number = new_number

    @property
    def mileage(self):
        """
        Getter Пробег автомобиля.
        :param mileage: Пробег Вашего автомобиля
        У стандартых автомобилей пробег неизвестен
        Примеры:
        >>> Auto = Auto("FORD", "S666-01", "GO88NO")
        """
        return self.mileage

    @mileage.setter
    def mileage(self, new_mileage):
        """
        Setter Пробег автомобиля.
        :param new_mileage: Новый пробег автомобиля
        :param mileage: Пробег Вашего автомобиля
        У стандартых автомобилей пробег неизвестен
        >>> Auto = Auto("FORD", "S666-01", "GO88NO")
        """
        self.new_mileage = new_mileage

class Auto_USA(Auto):
    """
    Создание и подготовка к работе объекта "Автомобиль из Америки"
    :param car_brand: Марка автомобиля
    :param serial_number: Серийный номер автомобиля
    :param number: Номер автомобиля (может состоять из неограниченног ичсла символов)
    Отличие от класса "Автомобиль" в том, что номер на автомобиле может иметь произвольную длину
    Примеры:
    >>> Auto_USA = Auto_USA("FORD", "S6666-01", "GO8NO")
    """
    def change_number(self, new_number) -> None:
        """
        Переопределение метода смены класса
        :return: None
        Примеры:
        >>> Auto_USA = Auto_USA("FORD", "S666-01", "GO8NO")
        """
        if not isinstance(new_number, str):
            raise TypeError("Номер автомобиля должен быть текстом")
        self.new_number = new_number

class Auto_used(Auto):
    def __init__(self, car_band: str, serial_number: str, number: str, mileage: int, cost: int):
        """
        Создание и подготовка к работе объекта "Автомобиль с пробегом"
        :param car_band: Марка автомобиля
        :param serial_number: Серийный номер
        :param number: Номер автомобиля из неограниченного числа символов
        :param mileage: Информация о пробеге автомобиля
        :param cost: Цена автомобиля
        Отличие от класса "Автомобиль" в том, что вводится параметр пробег автомобиля
        Примеры:
        >>> Auto_used = Auto_used("FORD", "S666-01", "GO88NO", 10000, 200000)
        """
        super().__init__(car_band, serial_number, number)
        self.mileage = mileage
        if not isinstance(cost, int):
            raise TypeError("Серийный номер должен быть текстом")
        self.cost = cost
    def transportation(self):
        """
        Функция расчета износа автомобиля
        Примеры:
        >>> Auto_used = Auto_used("FORD", "S666-01", "GO88NO", 10000, 200000)
        >>> Auto_used.transportation()
        """
        cost = self.cost * (1 / self.mileage)
        return cost

    def __str__(self):
        """
        Новое строковое представление, так как появился новый параметр
        >>> Auto_used = Auto_used("FORD", "S666-01", "GO88NO", 10000, 200000)
        >>> Auto_used.__str__()
        """
        return f"Марка автомобиля {self.car_brand}, Серийный номер автомобиля {self.serial_number}, " \
               f"Номер автомобиля {self.serial_number}, Пробег {self.mileage}"

if __name__ == "__main__":
    doctest.testmod()

Auto = Auto = Auto_used("FORD", "S666-01", "GO88NO", 10000, 200000)
print(Auto.__str__())
print(Auto.__repr__())


