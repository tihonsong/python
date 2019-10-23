"""
6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
   практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
   были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
   словарь на экран.
"""
import json

try:
    dict_subject_class_hour = {}
    with open("practice_6.txt") as file_obj:
        dict_subject = json.load(file_obj)
        for subject, dict_class in dict_subject.items():
            all_class_hour=0
            for class_name, class_hour in dict_class.items():
                all_class_hour+=class_hour
            dict_subject_class_hour[subject]=all_class_hour
    print(dict_subject_class_hour)

except FileNotFoundError:
    print("Данный файл не существует")