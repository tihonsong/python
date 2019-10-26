"""
2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
   атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
   массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
   для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
   Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        try:
            self._length, self._width = map(int, [length, width])
        except ValueError:
            print("Arguments have to number")

    def get_mass(self, depth):
        try:
            depth_cm = int(depth)
            mass = 12500000 / (self._length * self._width * depth_cm)
            return mass
        except ValueError:
            print("Depth is have to number")


road = Road(1000, 20)
print(f"Обязательно использовать масса асфальта {road.get_mass(5)} кг.")
