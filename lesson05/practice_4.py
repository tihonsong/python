"""
4) Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
    числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
try:
    wfile_obj = open("practice_4w.txt", "w")
    with open("practice_4.txt") as file_obj:
        dict_russian = {"one": "Один", "two": "Два", "three": "Три", "four": "Четырь"}
        for file_line in file_obj.readlines():
            num_eng, number = file_line.split(" — ")
            print(f"{dict_russian[num_eng.lower()]} — {int(number)}", file=wfile_obj)
except FileNotFoundError:
    print("Данный файл не существует!")
finally:
    wfile_obj.close()
