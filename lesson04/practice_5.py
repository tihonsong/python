"""
5) Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def sum_pair(prev_val, cur_val):
    return prev_val * cur_val


list_pair = [number_pair for number_pair in range(100, 1001) if number_pair % 2 == 0]

print(list_pair)

print(reduce(sum_pair, list_pair))
