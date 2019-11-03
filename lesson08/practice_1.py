"""
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
   В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
   преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
   и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    str_date = ''

    def __init__(self, str_date):
        MyDate.str_date = self.str_date = str_date

    @classmethod
    def get_my_date(cls):
        list_month = ["янв", "фвв", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        day, month, year = cls.str_date.split("-")
        month = list_month.index(month[:3].lower()) + 1 if month[:3].lower() in list_month else int(month)
        day, year = (int(day), int(year))

        return day, month, year

    @staticmethod
    def get_my_date_static(day, month, year):
        list_month = ["янв", "фвв", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        month = list_month.index(month[:3].lower()) + 1 if month[:3].lower() in list_month else int(month)
        day, year = (int(day), int(year))

        return day, month, year


obj_mydate = MyDate("01-01-2019")
print(obj_mydate.get_my_date())
print(MyDate.get_my_date_static("01", "Ноя", 2014))
