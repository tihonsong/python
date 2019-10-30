"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
   принимать данные (список списков) для формирования матрицы.Подсказка: матрица — система некоторых математических
   величин, расположенных в виде прямоугольной схемы.

   Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

   Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

   Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
   (двух матриц). Результатом сложения должна быть новая матрица.

   Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
   с первым элементом первой строки второй матрицы и т.д.

"""


class Matrix:
    def __init__(self, list_matrix):
        if type(list_matrix) == list:
            self.__matrix = list_matrix
        else:
            if type(list_matrix) != int:
                print('Have to list or number')
                exit(-1)

    def __str__(self):
        str_screen = ''
        for row in self.__matrix:
            for col in row:
                str_screen += (str(col) + " ")
            str_screen += "\n"
        return str_screen[:-1]

    def __add__(self, other_matrix):
        try:
            list_other = other_matrix if type(other_matrix) == list else other_matrix.get_matrix()
            sum_matrix = []
            idx_row = idx_col = 0
            for idx_row, val_row in enumerate(self.__matrix):
                if idx_row in range(len(list_other)):
                    sum_matrix.append([])
                    for idx_col, val_col in enumerate(val_row):
                        if idx_col in range(len(val_row)):
                            sum_matrix[idx_row].append(int(val_col) + int(list_other[idx_row][idx_col]))
                        else:
                            sum_matrix[idx_row].append(self.__matrix[idx_row][idx_col])
                    if idx_col < (len(list_other[idx_row])-1):
                        for idx in range(idx_col, (len(list_other[idx_row])-1)):
                            sum_matrix[idx_row].append(list_other[idx_row][idx])
                else:
                    sum_matrix.append(val_row)
            if idx_row < (len(list_other)-1):
                for idx in range(idx_row, (len(list_other)-1)):
                    sum_matrix.append(list_other[idx])

            return sum_matrix
        except AttributeError:
            print("Have to Matrix object")
        except ValueError:
            print("Element in matrix have to be number")

    def get_matrix(self):
        return self.__matrix


obj_matrix = Matrix([[31, 22], [37, 43], [51, 86]])
print(obj_matrix)
obj_matrix_other = Matrix([[1, 1], [1, 1], [1, 1], [1, 1]])
print(obj_matrix + obj_matrix_other)
