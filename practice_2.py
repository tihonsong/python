# 2)
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

list_user_input = input("Pls enter : ").split()

for idx, val in enumerate(list_user_input):
    if (idx+1) % 2 == 0:
        temp = list_user_input[idx-1]
        list_user_input[idx-1] = list_user_input[idx]
        list_user_input[idx] = temp

print(list_user_input)