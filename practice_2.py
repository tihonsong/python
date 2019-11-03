"""
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
   вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
   ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide_fun():
    try:
        val_1, val_2 = map(int, input("ВВодите 2 числа : ").split())
        if val_2 == 0:
            raise MyException("Второе число нельза 0!!")
        else:
            return val_1 / val_2
    except MyException as ex:
        print(ex)
        return divide_fun()


print(divide_fun())
