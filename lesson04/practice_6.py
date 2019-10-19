"""
6) Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count, cycle

for loop_number in count(0):
    print(loop_number)
#    if loop_number > 10:
#        break

list_string = ["abc", "def", "hij", "klm"]

# loop_num = 0
for str_value in cycle(list_string):
    print(str_value)
#    loop_num += 1
#    if loop_num > 10:
#        break
