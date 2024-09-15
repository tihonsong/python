# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
#    аргументов.


def my_func(number_1, number_2, number_3):
    list_number = [number_1, number_2, number_3]
    max_num_1 = max(list_number)
    list_number.remove(max_num_1)
    max_num_2 = max(list_number)

    return max_num_1 + max_num_2


try:
    print(my_func(int(input("Number1 :")), int(input("Number2 :")), int(input("Number3 :"))))
except ValueError:
    print("Нельза вводить строки!!!")
