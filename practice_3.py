"""
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
   income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
   например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе
   Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
   (get_full_profit). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
   проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    _name = ''
    _surname = ''
    _position = ''
    _income = {"profit": 0, "bonus": 0}

    def __init__(self, name, surname, pos):
        self._name = name
        self._surname = surname
        self._position = pos

    def set_profit(self, profit, bonus):
        try:
            self._income["profit"], self._income["bonus"] = map(int, [profit, bonus])
        except ValueError:
            print("Параметры обязательно чисел")
            exit()


class Position(Worker):
    def __init__(self, name, surname, pos):
        super().__init__(name, surname, pos)

    def get_full_name(self):
        return f"{self._surname} {self._name}"

    def get_full_profit(self):
        return sum([full_profit for key, full_profit in self._income.items()])


basic_info = input('Вводите Фамилия, Имя, Должность(Между ими вводите провел) : ').split()
salary_info = input('Вводите зарплата и примиум(Между ими вводите провел) : ').split()
position = Position(basic_info[1], basic_info[0], basic_info[2])
position.set_profit(salary_info[0], salary_info[1])

print(f"Уважаемые {position.get_full_name()} ваш полный доход {position.get_full_profit()} руб. в этом месяце")
