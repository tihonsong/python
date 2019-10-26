"""
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
   реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
   Время перехода между режимами должно составлять 7 и 2 секунды. Проверить работу примера, создав экземпляр и вызвав
   описанный метод.
"""
from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def running(self, mode_time1=7, mode_time2=2):
        try:
            mode_time1, mode_time2 = map(int, [mode_time1, mode_time2])
            for color in cycle(self.__color):
                if color in ("красный", "зеленый"):
                    print(color)
                    sleep(mode_time1)
                else:
                    print(color)
                    sleep(mode_time2)
        except ValueError:
            print("Arguments have to number")


light_control = TrafficLight()
light_control.running()
