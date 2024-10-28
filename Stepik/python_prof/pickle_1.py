# Найдите и исправьте ошибки, допущенные в приведенной ниже программе, чтобы она сериализовала словарь
# dogs и записала результат в файл dogs.pkl.

# import pickle
# dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}
# with open('pickle_1/dogs.pkl', mode='wb') as file:
#     pickle.dump(dogs, file)



# Дополните приведенный ниже код, чтобы для каждого кортежа из этого списка он вывел названия его полей и значения этих полей в следующем формате
# import pickle
# from collections import namedtuple
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
#
# with open('pickle_1/data.pkl', mode='rb') as file:
#     f = pickle.load(file)
#     for row in f:
#         for a, b in zip(Animal._fields, row):
#             print(f'{a}: {b}')
#         print()




# ополните приведенный ниже код, чтобы он вывел данные о каждом пользователе из этого списка, предварительно отсортировав
# их по статусу подписки от дорогой к дешевой, а при совпадении статусов — в лексикографическом порядке адресов электронных почт.
# Данные о каждом пользователе должны быть указаны в следующем формате:


# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
#
#
# for user in sorted(users, key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email)):
#     print(f'{user.name} {user.surname}\n'
#           f'  Email: {user.email}\n'
#           f'  Plan: {user.plan}\n')


# Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и
# времени встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.

# import csv
# from collections import namedtuple
# from datetime import datetime
# with open("pickle_1/meetings.csv", "r") as file:
#     f = csv.reader(file)
#     next(f)
#     patern = '%d.%m.%Y %H:%M'
#     Friends = namedtuple('Friends', ['name', 'date'])
#     friend = [Friends(n+' '+s, datetime.strptime(d+' '+t, patern)) for n, s, d, t in f]
#     for row in sorted(friend, key=lambda x: x.date):
#         print(row.name)



# Дан pickle файл, содержащий единственную сериализованную функцию. Напишите программу,
# которая вызывает данную функцию с заданными аргументами и выводит возвращаемое значение функции.

# import pickle
# import sys
# d = [i.strip() for i in sys.stdin]
# with open(d.pop(0), "rb") as file:
#     f = pickle.load(file)
#     print(f(*d))


# Функция должна создавать pickle файл с названием filename,
# который содержит сериализованный список только тех объектов из списка objects, тип которых равен typename.


# import pickle
# def filter_dump(filename, objects, typename):
#     with open(filename, 'wb') as f:
#         pickle.dump(list(filter(lambda x: isinstance(x, typename), objects)), f)



# Напишите программу, которая вычисляет контрольную сумму для объекта, содержащегося в pickle файле, и сравнивает ее с данным целым числом.

import pickle

res = {
    True: 'Контрольные суммы совпадают',
    False: 'Контрольные суммы не совпадают'
}

with open(input(), "rb") as f:
    data = pickle.load(f)
    if isinstance(data, dict):
        print(res[sum(filter(lambda x: isinstance(x, int), data.keys())) == int(input())])
    elif isinstance(data, list):
        k = list(filter(lambda x: isinstance(x, int), data))
        print(res[max(k, default=0) * min(k, default=0) == int(input())])




