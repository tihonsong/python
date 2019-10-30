"""
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
   конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
   реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
   (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
   уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно
   осуществляться округление значения до целого числа.

   Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

   Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
   больше нуля, иначе выводить соответствующее сообщение.

   Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
   этих двух клеток.

   Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
   ячеек этих двух клеток.

   В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
   метод позволяет организовать ячейки по рядам.

   Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
   аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

   Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
   *****\n*****\n**.

   Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
   *****\n*****\n*****.

   Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Grid:
    def __init__(self, count_cell):
        try:
            self.__cells = '*' * int(count_cell)
        except ValueError:
            print("Количесмтво обязательно чисел")
            exit(-1)

    def __add__(self, other_grid):
        try:
            cells = other_grid.get_cells()
            return Grid(len(self.__cells) + len(cells))
        except AttributeError:
            print("Только Grid обьекта разрешает")
            exit(-1)

    def __sub__(self, other_grid):
        try:
            cells = other_grid.get_cells()
            if len(self.__cells) - len(cells) <= 0:
                print("Не может вычисляться")
                exit(-1)
            else:
                return Grid(len(self.__cells) - len(cells))
        except AttributeError:
            print("Только Grid обьекта разрешает")
            exit(-1)

    def __mul__(self, other_grid):
        try:
            cells = other_grid.get_cells()
            return Grid((len(self.__cells) * len(cells)))
        except AttributeError:
            print("Только Grid обьекта разрешает")
            exit(-1)

    def __truediv__(self, other_grid):
        try:
            cells = other_grid.get_cells()
            return Grid(round(len(self.__cells) / len(cells)))
        except AttributeError:
            print("Только Grid обьекта разрешает")
            exit(-1)
        except ZeroDivisionError:
            print("Нельза без ячейку")
            exit(-1)

    def get_cells(self):
        return self.__cells

    def make_order(self, col_count):
        loop_count = len(self.__cells) // col_count
        remained = len(self.__cells) % col_count
        order = ''
        for iter in range(loop_count):
            order += ('*' * col_count) + '\n'
        return order + ('*' * remained)


obj_grid1 = Grid(10)
obj_grid2 = Grid(5)
obj_mul_grid = obj_grid1 * obj_grid2

print(obj_mul_grid.make_order(8))
