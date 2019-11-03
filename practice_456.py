"""
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
   который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
   базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
   уникальные для каждого типа оргтехники.

5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
   определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
   других данных, можно использовать любую подходящую структуру, например словарь.

6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
   указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
   Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
   уроках по ООП.
"""
from abc import ABC, abstractmethod


class StoreExeption(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquip(ABC):
    def __init__(self):
        self._width = 0
        self._height = 0
        self._depth = 0
        self._company_name = ''
        self._equip_dict = {}

    def input_characteristic(self):
        try:
            self._company_name = input("Вводите названия производители : ")
            self._width, self._height, self._depth = map(int, input("Вводите Ш х В х Г (мм): ").split(','))
            self._input_char_by_equip()
        except ValueError:
            print("Только чисел !!")
            self.input_characteristic()

    @abstractmethod
    def _input_char_by_equip(self):
        pass

    @property
    def equip_character(self):
        self._equip_dict = {"name_of_comp": self._company_name, "width": self._width, "height": self._height,
                            "depth": self._depth}
        self._equip_char_by_equip()
        return self._equip_dict

    @abstractmethod
    def _equip_char_by_equip(self):
        pass


class Scanner(OfficeEquip):
    def __init__(self):
        super().__init__()
        self.dpi = ''
        self.dict_characteristic = {}

    def _input_char_by_equip(self):
        self.dpi = input("Вводите DPI:")

    def _equip_char_by_equip(self):
        self._equip_dict["dpi"] = self.dpi


class Printer(OfficeEquip):
    def __init__(self):
        super().__init__()
        self._is_ethernet = False

    def _input_char_by_equip(self):
        try:
            self._is_ethernet = input("Есть Ethernet (Есть, Нет):")
            if self._is_ethernet.lower() != 'есть' and self._is_ethernet.lower() != 'нет':
                raise StoreExeption("Только Есть или Нет!!")
        except StoreExeption as ex:
            print(ex)
            self._input_char_by_equip()

    def _equip_char_by_equip(self):
        self._equip_dict["is_ethernet"] = self._is_ethernet


class Copier(OfficeEquip):
    def __init__(self):
        super().__init__()
        self._speed = ''

    def _input_char_by_equip(self):
        self.speed = input("Вводите скорость: ")

    def _equip_char_by_equip(self):
        self._equip_dict["speed"] = self._speed


class Store:
    def __init__(self):
        self._row = 0
        self._col = 0
        self._count_equip = ''
        self._for_who = ''
        self._equip = object
        self._list_equip = [Printer(), Scanner(), Copier()]

    def _input_location(self):
        try:
            self._row, self._col = map(int, input("Location in store(Row, Col) : ").split(','))
        except ValueError:
            print("Only number !!")
            self._input_location()

    def _input_count_equip(self):
        try:
            self._count_equip = int(input("Вводите количество оборудованиях(шт.) : "))
        except ValueError:
            print("Only number !!")
            self._input_count_equip()

    def _input_type_of_euip(self):
        try:
            num_of_equip = int(input("Выбрайте тип оборудования - 1) Принтер 2) Сканнер 3) Ксерокс : "))
            if num_of_equip < 1 or num_of_equip > 3:
                raise StoreExeption("Только 1,2,3")
        except ValueError:
            print("Только чисел!!")
            return self._input_type_of_euip()
        except StoreExeption as ex:
            print(ex)
            return self._input_type_of_euip()
        else:
            return self._list_equip[num_of_equip - 1]

    def save_in_store(self):
        self._input_location()
        self._input_count_equip()
        self._for_who = input("На какой департамент нужно отправить ? : ")
        self._equip = self._input_type_of_euip()
        self._equip.input_characteristic()

    @property
    def equip_in_store(self):
        return {'row': self._row, 'col': self._col, 'count': self._count_equip, 'equip': self._equip.equip_character,
                'for_who': self._for_who}


list_equip = []
is_end = False
obj_store = Store()

while not is_end:
    obj_store.save_in_store()
    list_equip.append(obj_store.equip_in_store)
    if input("Продольжаете (Да/Нет)? ").lower() == "нет":
        is_end = True

print(list_equip)
