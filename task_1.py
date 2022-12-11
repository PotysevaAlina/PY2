import doctest


class Bacteria:
    def __init__(self, volume: float, genome_size: int):
        """
        Создание и подготовка к работе объекта "Бактерия"
        :param volume: Объем клетки в мкм^3
        :param genome_size: Размер генома бактерии в п.о.
        Примеры:
        >>> bacteria = Bacteria(0.6, 4600000) # инициализация экземпляра класса
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем бактерии должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем бактерии должен быть положительным числом")
        self.volume = volume

        if not isinstance(genome_size, int):
            raise TypeError("Размер генома бактерии должен быть типа int")
        if genome_size <= 0:
            raise ValueError("Размер генома бактерии должен быть положительным числом")
        self.genome_size = genome_size

    def is_unreal_bacteria(self) -> bool:
        """
        Функция, которая проверяет являются ли заданные параметры удобоваримыми для существования бактерии
        :return: Существует ли бактерия
        Примеры:
        >>> bacteria = Bacteria(0, 4600000)
        >>> bacteria.is_unreal_bacteria()
        """

    def add_mutations_to_genome(self, add_mutations: int) -> None:
        """
        Добавление мутаций в геном
        :param add_mutations: Количество добавляемых мутаций
        :raise ValueError: Если количество мутаций больше половины длины генома
        Примеры:
        >>> bacteria = Bacteria(0.6, 4600000)
        >>> bacteria.add_mutations_to_genome(36)
        """
        if not isinstance(add_mutations, int):
            raise TypeError("Добавляемое число мутаций должно быть типа int")
        if add_mutations < 0:
            raise ValueError("Добавляемое число мутаций должно быть положительным числом")

    def remove_base_pairs_from_genome(self, remove_base_pairs: int) -> bool:
        """
        Удаление пар оснований из генома
        :param remove_base_pairs: Количество удаляемых пар оснований
        :return: Возможно ли удалить такое количество пар оснований
        Примеры:
        >>> bacteria = Bacteria(0.6, 4600000)
        >>> bacteria.remove_base_pairs_from_genome(4500)
        """

        if not isinstance(remove_base_pairs, int):
            raise TypeError("Удаляемое число пар оснований должно быть типа int")
        if remove_base_pairs < 0:
            raise ValueError("Удаляемое число пар оснований должно быть положительным числом")

class Human:
    def __init__(self, height: float, weight: float):
        """
        Создание и подготовка к работе объекта "Человек"
        :param height: Рост в см
        :param weight: Вес в кг
        Примеры:
        >>> human = Human(160.5, 60.2) # инициализация экземпляра класса
        """

        if not isinstance(height, (int, float)):
            raise TypeError("Рост человека должен быть типа int или float")
        if height <= 0:
            raise ValueError("Рост человека должен быть положительным числом")
        self.height = height

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес человека должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес человека должен быть положительным числом")
        self.weight = weight

    def is_unhealthy_haman(self) -> bool:
        """
        Функция, которая проверяет является ли человек здоровым
        :return: Здоров ли человек
        Примеры:
        >>> human = Human(160, 200)
        >>> human.is_unhealthy_haman()
        """

    def add_weight(self, add_weight: float) -> None:
        """
        Набор веса
        :param add_weight: Вес, который необходимо набрать
        :raise ValueError: Если вес равен больше, чем число, получаемое при вычетании 100 из роста
        Примеры:
        >>> human = Human(160.5, 45)
        >>> human.add_weight(10)
        """
        if not isinstance(add_weight, (int, float)):
            raise TypeError("Добавляемый вес должен быть типа int или float")
        if add_weight < 0:
            raise ValueError("Добавляемый вес должен быть положительным числом")


    def remove_weight(self, remove_weight: float) -> bool:
        """
        Снижение веса
        :param remove_weight: Количество снижаемого веса
        :return: Нужно ли сбрасывать вес
        Примеры:
        >>> human = Human(160.5, 100)
        >>> human.remove_weight(50.8)
        """

        if not isinstance(remove_weight, float):
            raise TypeError("Снижаемый вес должен быть типа int или float")
        if remove_base_pairs < 0:
            raise ValueError("Снижаемый вес должен быть положительным числом")

class Purchase:
    def __init__(self, quantity, price):
        self.quantity = int(quantity)
        if not isinstance(price, (int, float)):
            raise TypeError("Введенная цена должна быть типом int или float")
        self.price = price
    def discount(self, price, quantity):
        if price >= quantity * 8:
            price == price * 0.9
    def cost_purchase(self):
        return self.price
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации