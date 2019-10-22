"""
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
   кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
   дохода сотрудников.
"""
try:
    with open("practice_3.txt") as file_obj:
        count_worker = 0
        sum_salary = 0
        while True:
            file_line = file_obj.readline()
            if file_line == '':
                print("-" * 100)
                print(f"Средный зарплатат : {sum_salary / count_worker:.02f}")
                break

            name, salary = file_line.split(":")
            salary = int(salary)
            if salary < 20000:
                count_worker += 1
                sum_salary += salary
                print(f"{name}: {salary}")

except FileNotFoundError:
    print("Данный файл не существует!")
except ValueError:
    print("Заплата нужно число!")
