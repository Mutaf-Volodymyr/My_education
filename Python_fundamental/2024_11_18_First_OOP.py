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


class Person:
    count_persons = 0

    def __init__(self, name):
        self.name = name
        self.count_persons += 1

p1 = Person("sfd")
p2 = Person("sfd")
p3 = Person("sfd")
print(Person.count_persons)
print(p1.count_persons)
print(p2.count_persons)
print(p3.count_persons)


