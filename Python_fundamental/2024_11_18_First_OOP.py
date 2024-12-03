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


# from datetime import date
#
#
# class Person:
#     def __init__(self, name: str, birth_date: date):
#         self.name = name
#         self.birth_date = birth_date
#         self.working = False
#
#     def __str__(self):
#         return f'{self.name} {self.birth_date}'
#
#     def get_age(self):
#         today = date.today()
#         age = today.year - self.birth_date.year
#         if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
#             age -= 1
#         return age
#
#     def is_adulthood(self):
#         return True if self.get_age() >= 18 else False
#
#
# # сначала создал через функцию super
# # class Employee(Person):
# #     def __init__(self, person):
# #         super().__init__(person.name, person.birth_date)
# # но изменения Person не затрагивали Employee. Учитывая то, что Employee формируются из Person и любые изменения в
# # Person должны изменять Employee, то было принято решение сделать так.
#
# class Employee:
#     def __init__(self, person):
#         self.person = person
#         person.working = True
#
#     def __str__(self):
#         return f'{self.person.name} {self.person.birth_date}'
#
#
# persons = [vova := Person('11111111', date(1990, 5, 2)),
#            lena := Person('Lena', date(1996, 12, 3)),
#            andrey := Person('Andrey', date(1999, 1, 31)),
#            mark := Person('Mark', date(2016, 3, 28)),
#            jim := Person('Jim', date(2004, 1, 15)),
#            kiril := Person('Kiril', date(2018, 6, 13)),
#            anton := Person('Anton', date(2005, 7, 11)),
#            ivan := Person('Ivan', date(1984, 5, 6)),
#            olha := Person('Olha', date(2012, 9, 9)),
#            lili := Person('Lili', date(2020, 11, 2))]
#
# employees = list(map(Employee, (filter(lambda x: x.is_adulthood(), persons))))
#
# vova.name = 'Vova'
#
# print(*employees, sep='\n')
# print(kiril.working)
# print(ivan.working)
# print(all(employee.person.get_age() >= 18 for employee in employees))


# class Person:
#     count_persons = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.count_persons += 1
#
# p1 = Person("sfd")
# p2 = Person("sfd")
# p3 = Person("sfd")
# print(Person.count_persons)
# print(p1.count_persons)
# print(p2.count_persons)
# print(p3.count_persons)




# import time
# def slip_for_time(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator
#
#
# @slip_for_time(10)
# def my_function(a=5):
#     return a
#
# # function = decorator(my_function)
#
# print(dir(my_function))



####################################


class My_class:
    class_attr = "hallo"

    @classmethod
    def class_method(cls):
        print(cls.class_attr)

    @staticmethod
    def static_method():
        print('static method')

# a = My_class()
# a.class_method()
# print(a.class_attr)


######################


# 1. Создайте абстрактный класс Plant, которого есть 3 свойства: display_name (читаемое
# название), текущая высота (height), текущий возраст (age).

from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, name, height, age):
        self.__name = name
        self.__height = height
        self.__age = age


    def display_name(self):
        print(self.__name)

    def display_info(self):
        print(f'Class: {self.__class__.__name__}\n'
                f'\t{self.__name}\n'
                f'\t{self.__height}\n'
                f'\t{self.__age}')


    @abstractmethod
    def grow_per_season(self):
        pass






class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.__color = color

    def grow_per_season(self):
        pass

    def display_info(self):
        super().display_info()
        print(f'\t{self.__color}\n')


class Tree(Plant):
    def grow_per_season(self):
        pass



rose = Flower(name='Rose', height=100, age=1, color='red')
rose.display_info()


# 2. У классов Flower и Tree есть приватные статические атрибуты flower_grow_per_season и
# tree_grow per_season соответственно. У класса Plant есть абстрактный метод
# grow_per_season(), который переопределен в подклассах и возвращает соответствующее
# статическое значение. Подумайте, почему статические атрибуты приватны и зачем нам
# нужен абстрактный метод grow_per_season()? Почему создание обычного метода тут не
# очень подходит?






















