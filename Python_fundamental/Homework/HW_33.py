# 1. Реализуйте класс Employee, представляющий сотрудника компании.
# Класс должен иметь статическое поле company с названием компании, а также методы:
# set_company(cls, name): метод класса для изменения названия компании
# __init__(self, name, position): конструктор, принимающий имя и должность сотрудника
# get_info(self): метод, возвращающий информацию о сотруднике в виде строки (имя, должность, название компании)


class Employee:
    __company = 'Bayerische Motoren Werke'

    @classmethod
    def set_company(cls, name):
        cls.__company = name

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f'{self.name}, {self.position}, {self.__company}'


employee1 = Employee("John", "Manager")
employee2 = Employee("Alice", "Developer")

print(employee1.get_info())
Employee.set_company("XYZ Company")
print(employee2.get_info())



# 2. Реализуйте абстрактный базовый класс Shape (фигура),
# а от него унаследуйте классы Rectangle (прямоугольник) и Circle (круг).
# Класс Shape должен иметь абстрактный метод area, который должен быть реализован в каждом дочернем классе.
# Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра.
# Выведите площадь и периметр прямоугольника и круга на экран.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius


rectangle = Rectangle(5, 3)
circle = Circle(2)
print(f"Rectangle area: {rectangle.calculate_area()}")  # Вывод: Rectangle area: 15
print(f"Rectangle perimeter: {rectangle.calculate_perimeter()}")  # Вывод: Rectangle perimeter: 16
print(f"Circle area: {circle.calculate_area()}")  # Вывод: Circle area: 12.566370614359172
print(f"Circle perimeter: {circle.calculate_perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172