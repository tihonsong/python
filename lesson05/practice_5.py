"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
   подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open("practice_5.txt", "a") as file_obj:
    gen_count = 0
    sum_random_number = 0
    while gen_count <= 20:
        gen_count += 1
        random_number = random.randint(1, 40)
        sum_random_number += random_number
        print(f"{random_number} ", end='', file=file_obj)

print("Сумма чисел : ", sum_random_number)
