# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#
# cars = [car1 := Car("Kia", 2016, "Purple"),
#         car2 := Car("Toyota", 2015, "Red"),
#         car3 := Car("BMW", 2020, "Blue"),
#         car4 := Car("Ford", 2018, "Black"),
#         car5 := Car("Audi", 2023, "White"),
#         car6 := Car("Honda", 2010, "Silver"),
#         car7 := Car("Tesla", 2021, "Green"),
#         car8 := Car("Nissan", 2005, "Gray"),
#         car9 := Car("Volkswagen", 2019, "Yellow"),
#         car10 := Car("Chevrolet", 2017, "Orange")]
#
#
#
# def get_color_car(auto_list:list, color:str):
#     return list(filter(lambda car: car.color == color, auto_list))
#
# for car in get_color_car(cars, color='Black'):
#     print(car.model, car.year, car.color)


# 5. Создать класс Person с полями имя и дата рождения.
# 6. Создать 10 объектов этого класса с разными именами.
# 7. Создать класс Employee который содержит поле имя и возраст.
# 8. Написать функцию, которая из списка объекта класса Person создает список из объектов
# класса Employee, вычисляя возраст каждого Person по дате рождения.
# Подумать, где должна быть реализована функция, вычисляющая возраст по дате рождения.
# Варианты: в конструкторе класса Employee, в качестве глобальной функции, в качестве
# метода класса (какого?. Получившийся список должен содержать сотрудников, старше 18
# лет. Использовать map и filter. У классов Person и Employee должны быть определены
# конструкторы. Реализация трансформации список персонов в сотрудников должна быть в
# одну строчку.
# 9. Вывести получившихся сотрудников на экран.
# 10. Используя функцию forAll() убедиться, что все сотрудники действительно старше 18 лет.


from datetime import date, timedelta


class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Person:
    def __init__(self, name: str, birthday: date):
        self.name = name
        self.birthday = birthday

    def get_age(self):
        return int((date.today() - self.birthday).days / 365.25)

    def make_employee(self):
        return Employee(self.name, self.get_age())


vova = Person('vova', date(1990, 5, 2))
lena = Person('lena', date(1996, 12, 3))
andrey = Person('andrey', date(1999, 1, 31))
