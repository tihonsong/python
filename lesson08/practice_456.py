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


class StoreExeption(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:
    def __init__(self):
        self._row = 0
        self._col = 0
        self._kind_of_equip = ''
        self._col = 0

    def _input_location(self):
        try:
            self.row, self.col = map(int, input("Location in store(Row, Col) : "))
        except ValueError:
            print("Only number !!")
            self._input_location()

    def _input_size(self):
        pass


class OfficeEquip:
    def __init__(self, width, high, depth):
        self._width = width
        self._high = high
        self._depth = depth


class Scanner(OfficeEquip):
    def __init__(self, *args, dpi):
        super().__init__(args[0], args[1], args[2])
        self.dpi = dpi


class Printer(OfficeEquip):
    def __init__(self, *args, is_ethernet):
        super().__init__(args[0], args[1], args[2])
        self.is_ethernet = is_ethernet


class Copier(OfficeEquip):
    def __init__(self, *args, speed):
        super().__init__(args[0], args[1], args[2])
        self.speed = speed
