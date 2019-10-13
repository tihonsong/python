# 3)
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

list_time_of_year = ["Зима", "Весна", "Лето", "Осень"]
list_group_month = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
month = 0

while not ((1 <= month) and (month <= 12)):
    month = int(input("Вводите месяцу (01 - 12): "))
    if (1 <= month) and (month <= 12):
        continue
    print("Неправильная цифира!")

for idx, grp in enumerate(list_group_month):
    if month in grp:
        time_of_year = list_time_of_year[idx]
        break

print(time_of_year)

# dict_time_of_year = zip(list_time_of_year, list_group_month)
dict_time_of_year = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}

for key, grp in dict_time_of_year.items():
    if month in grp:
        time_of_year = key
        break

print(time_of_year)
