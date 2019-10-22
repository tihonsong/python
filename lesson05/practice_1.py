"""
1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
   ввода данных свидетельствует пустая строка.
"""
try:
    with open("practice_1.txt", "x") as file_obj:
        while True:
            user_str = input("Вводите строки (Пустая строка завершит ввод) : ")
            if user_str == '':
                break
            file_obj.write(user_str+'\n')

except FileExistsError:
    print("Данный файл есть !!")
