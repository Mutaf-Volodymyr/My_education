# Реализуйте функцию calculate_it(), которая принимает один или более аргументов в следующем порядке:
#
# func — произвольная функция
# *args — переменное количество позиционных аргументов, каждый из которых является произвольным объектом
# Функция должна возвращать кортеж, первым элементом которого является возвращаемое значение функции func
# при вызове с аргументами *args, а вторым — примерное время (в секундах), затраченное на вычисление этого значения.

import time
from operator import index


def calculate_it(func, *args):
    start_time = time.perf_counter()
    res = func(*args)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return res, elapsed_time




# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
#
# funcs — список произвольных функций
# arg — произвольный объект
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на
# вычисление значения при вызове с аргументом arg наименьшее количество времени.

# import time
# def get_the_fastest_func(funcs, arg):
#     res = {}
#     for func in funcs:
#         start_time = time.perf_counter()
#         func(arg)
#         end_time = time.perf_counter()
#         elapsed_time = end_time - start_time
#         res[elapsed_time] = func
#     return res


#########################
# Напишите программу, которая определяет, является ли год високосным.
# import calendar
# for _ in range(int(input())):
#     print(calendar.isleap(int(input())))


# Напишите программу, которая выводит календарь на заданные год и месяц.
# import calendar
# d = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
# y, m = input().split()
# calendar.prmonth(int(y), d[m])


# Напишите программу, которая определяет день недели, соответствующий заданной дате.
# import calendar
# d = calendar.weekday(*map(int, input().split('-')))
# print(list(calendar.day_name)[d])

# Напишите программу, которая определяет количество дней в заданном месяце.
# import calendar
# print(calendar.monthrange(*map(int, input().split()))[1])

# На вход программе подаются год и полное название месяца на английском, разделенные пробелом.
# import calendar
# y, m = input().split()
# l = list(calendar.month_name)
#
# print(calendar.monthrange(int(y), l.index(m))[1])


# Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
#
# year — натуральное число
# month — полное название месяца на английском
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

# import calendar
# from datetime import date
# def get_days_in_month(year:int, month:str):
#     m = list(calendar.month_name)
#     m = m.index(month)
#     r = calendar.monthrange(year, m)[1]
#     res = []
#     for i in range(1, r+1):
#         res.append(date(year, m, i))
#     return res



# Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
#
# year — натуральное число
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.

# import calendar
# from datetime import date
# def get_all_mondays(year):
#     res = []
#     for m in range(1, 13):
#         mr = calendar.monthrange(year, m)[1]
#         for d in range(1, mr+1):
#             dat = date(year, m, d)
#             if dat.weekday() == 0:
#                 res.append(dat)
#     return res



# Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных
# категорий граждан происходит без взимания платы. Например, в Эрмитаже это третий четверг месяца.
# Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.

# import calendar
# from datetime import date
# year = int(input())
# pattern = '%d.%m.%Y'
# res = []
# for m in range(1, 13):
#     mr = calendar.monthrange(year, m)[1]
#     count = 0
#     for d in range(1, mr+1):
#         dat = date(year, m, d)
#         if dat.weekday() == 3:
#             count += 1
#         if count == 3:
#             res.append(dat)
#             count = 0
#             break
#
# for dat in res:
#     print(dat.strftime(pattern))



# Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
#
# year — натуральное число, год
# Функция должна возвращать количество воскресений в году year.


# import calendar
# from datetime import date
# def num_of_sundays(year):
#     count = 0
#     for m in range(1, 13):
#         mr = calendar.monthrange(year, m)[1]
#         for d in range(1, mr+1):
#             if date(year, m, d).weekday() == 6:
#                 count += 1
#     return count

