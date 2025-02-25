__author__ = 'Сон Чихок'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
numbers = int(input("Please enter number : "))
max_num = 0
while numbers != 0:
    number = numbers % 10
    if number > max_num:
        max_num = number
    numbers = numbers // 10

print(max_num)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
number_1 = input("Please enter number1 : ")
number_2 = input("Please enter number2 : ")
print(number_1, number_2)

number_1 = int(number_1 + number_2)
number_2 = number_1 - int(number_2)
number_1 = -(number_2 - number_1)
while number_2 % 10 == 0:
    number_2 = number_2 // 10

print(number_1, number_2)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math

number_a = int(input("Please enter a : "))
number_b = int(input("Please enter b : "))
number_c = int(input("Please enter c : "))

minus_x = (-number_b - math.sqrt(abs(number_b ** 2 - 4 * number_a * number_c))) / 2 * number_a
plus_x = (-number_b + math.sqrt(abs(number_b ** 2 - 4 * number_a * number_c))) / 2 * number_a

print(minus_x, plus_x)
