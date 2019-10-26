"""
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
   (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
   Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
   выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
   экземпляра.
"""


class Stationery:
    _msg = "отрисутеся"

    def __init__(self, title):
        self._title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        super().__init__("ручка")

    def draw(self):
        print(f"{self._title} {self._msg} что-то какие-то")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("карандаш")

    def draw(self):
        print(f"{self._title} {self._msg} что-то какие-то")


class Handle(Stationery):
    def __init__(self):
        super().__init__("маркер")

    def draw(self):
        print(f"{self._title} {self._msg} что-то какие-то")


obj_stationery = Stationery("")
obj_stationery.draw()

obj_stationery = Pen()
obj_stationery.draw()

obj_stationery = Pencil()
obj_stationery.draw()

obj_stationery = Handle()
obj_stationery.draw()
