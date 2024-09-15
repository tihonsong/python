# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
#    у пользователя, предусмотреть обработку ситуации деления на ноль.


def divide_number():
    try:
        print(int(input("First: ")) / int(input("Second: ")))

    except ZeroDivisionError:
        print("Не правильно число!")
    except ValueError:
        print("Не можете вводить строки")


divide_number()
