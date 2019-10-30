"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
   — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
   типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
   соответственно.

   Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
   (2*H + 0.3). Проверить работу этих методов на реальных данных.

   Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
   абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import abstractmethod


class Cloth:
    def __init__(self, name_of_maker):
        self._name_of_maker = name_of_maker

    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Cloth):
    def __init__(self, name_of_maker, size):
        super().__init__(name_of_maker)
        self.__V = size

    @property
    def calc_cloth(self):
        try:
            return f"Сумма расхода ткани для пальта {self._name_of_maker} - {round((int(self.__V) / 6.5) + 0.5,2)}"
        except ValueError:
            print("Размер обязательно чисел")


class Suit(Cloth):
    def __init__(self, name_of_maker, length):
        super().__init__(name_of_maker)
        self.__H = length

    @property
    def calc_cloth(self):
        try:
            return f"Сумма расхода ткани для костюм {self._name_of_maker} - {(int(self.__H * 2)) + 0.3}"
        except ValueError:
            print("Размер обязательно чисел")


obj_suit = Suit('Almani', 100)
print(obj_suit.calc_cloth)

obj_suit = Coat('Твое', 44)
print(obj_suit.calc_cloth)
