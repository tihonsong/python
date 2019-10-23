"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
   количества слов в каждой строке.
"""

try:
    with open("practice_2.txt") as file_obj:
        line_counter = 0
        while True:
            contents_line = file_obj.readline()
            if contents_line == '':
                break
            line_counter += 1
            print(f"Номер строки : {line_counter}) {contents_line[:-1]}, Количество букв : {len(contents_line)}")

except FileNotFoundError:
    print("Нет данный файл!!")

