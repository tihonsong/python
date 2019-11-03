"""
3) Создайте собственный класс-исключение, который должен проверять содержимое списка на отсутствие элементов типа
   строка и булево. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и
   заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyClass:
    def __init__(self):
        self.my_list = []

    def list_func(self):
        try:
            str_input = input("ВВодите 2 числа : ")
            if str_input == '':
                return self.my_list

            if str_input.lower() == 'true' or str_input.lower() == 'false':
                raise MyException('Нельза булево!!')
            elif '.' in str_input:
                str_input = float(str_input)
            else:
                str_input = int(str_input)
        except ValueError:
            print("Строки нельза")
            self.list_func()
        except MyException as ex:
            print(ex)
            self.list_func()
        finally:
            self.my_list.append(str_input)
            self.list_func()


obj_myclass = MyClass()
obj_myclass.list_func()