""""
7) Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen(). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fibo_gen(user_num):
    for seq_num in range(user_num, user_num + 15):
        yield seq_num


try:
    user_num = int(input("Вводите число : "))

    fac_num = 1
    string_print = ''

    for el in fibo_gen(user_num):
        string_print += str(el) + " * "
        fac_num *= el

    print(f"{string_print[:-2]} = {fac_num}")
except ValueError:
    print("Только число !!!")
