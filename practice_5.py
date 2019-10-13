# 5)
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
# новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
user_val = int(input("Цифра : "))
is_find = False

for idx, val in enumerate(my_list):
    if user_val > val:
        is_find = True
        my_list.insert(idx, user_val)
        break
    elif user_val == val:
        idx_second = idx + 1
        while True:
            if user_val != my_list[idx_second]:
                break
            idx_second += 1
        is_find = True
        my_list.insert(idx_second, user_val)
        break

if not is_find:
    my_list.append(user_val)

print(my_list)