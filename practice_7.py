"""
7) Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
   собственности, выручка, издержки. Необходимо вычислить прибыль каждой компании и среднюю прибыль. Реализовать список,
   содержащий словарь (название фирмы и прибыль) и словарь с одним элементом (средняя прибыль). Добавить в первый словарь
   еще один элемент, содержащий результат вычисления отношения прибыли к убыткам. Итоговый список сохранить в файл.
   Подсказка: использовать менеджеры контекста.
"""
import json

try:
    with open("practice_7.txt", "r+") as file_obj:
        list_company = json.load(file_obj)
        profit = 0
        loss = 0
        list_comp = []
        for idx, dict_company_info in list_company.items():
            revenue = int(dict_company_info["выручка"])
            cost = int(dict_company_info["издержки"])
            list_comp.append({"название": dict_company_info["название"], "прибыли": revenue - cost})
            profit += revenue - cost if revenue - cost > 0 else 0
            loss += abs(revenue - cost) if revenue - cost < 0 else 0
        loss = loss if loss != 0 else 1
        list_comp.append({"средняя прибыль": round((profit - loss) / len(list_company), 2)})
        list_comp.insert(0, {"отношения прибыли к убыткам": str(round((profit / loss) * 100, 2)) + "%"})

        print(f"\n{list_comp}", file=file_obj)

except FileNotFoundError:
    print("Данный файл не существует!")
except ValueError:
    print("Выручка и изедржки обязательно чисел")
except ZeroDivisionError:
    print("Нет убыток")
