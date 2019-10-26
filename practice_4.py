"""
4) Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть следующие атрибуты:
   speed, color, name, is_police (булево). А также несколько методов: go, stop, turn(direction), которые должны
   сообщать, что машина поехала, остановилась, повернула (куда).
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print(f"{self._name}({'Полис' if self._is_police else 'обычная'}) поехала по {self._speed} км в час")

    def stop(self):
        print(f"{self._name} остановилась")

    def turn(self, direction):
        print(f"{self._name} повернула {direction}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


my_car = WorkCar(60, "Синий", "Моя машина")
my_car.go()
my_car.stop()
my_car.turn("налево")
