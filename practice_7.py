"""
7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
   методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
   числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class MyComplexException(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyComplex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_comp):
        if other_comp.__class__ != MyComplex:
            raise MyComplexException("Have to MyComplex Class")
        else:
            return MyComplex(self.x + other_comp.x, self.y + other_comp.y)

    def __mul__(self, other_comp):
        if other_comp.__class__ != MyComplex:
            raise MyComplexException("Have to MyComplex Class")
        else:
            x = self.x * other_comp.x
            y = (self.x * other_comp.y) + (self.y * other_comp.x)
            x += -(self.y * other_comp.y)
            return MyComplex(x, y)

    def __str__(self):
        return f"{self.x}+{self.y}j"


class TestClass:
    def __init__(self, comp_1, comp_2):
        self.obj_mycomp_1, self.obj_mycomp_2 = comp_1, comp_2

    def add(self):
        return self.obj_mycomp_1 + self.obj_mycomp_2

    def mul(self):
        return self.obj_mycomp_1 * self.obj_mycomp_2


obj_test = TestClass(MyComplex(1, 2), object)
try:
    print(obj_test.add())
    print(obj_test.mul())
except MyComplexException as ex:
    print(ex)
