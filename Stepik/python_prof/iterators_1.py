# Вам доступен список numbers, содержащий целые числа. Дополните приведенный ниже код с
# использованием функций iter() и next(), чтобы он вывел четвертый элемент данного списка.
# from random import randint

from symtable import Class
from typing import Iterable


# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62,
#            64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
# n = iter(numbers)
# next(n)
# next(n)
# next(n)
# print(next(n))


####################################################
# Реализуйте функцию filterfalse() с использованием функции filter(), которая принимает два аргумента:
# predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
# iterable — итерируемый объект
# Функция должна работать противоположно функции filter(), то есть возвращать итератор, элементами
# которого являются элементы итерируемого объекта iterable, для которых функция predicate вернула значение False.
# def filterfalse(predicate, iterable):
#     if predicate is None:
#         predicate = bool
#     return iter(i for i in iterable if not predicate(i))





####################################################
# Реализуйте функцию transpose() с использованием функции zip(), которая принимает один аргумент:
#
# matrix — матрица произвольной размерности
# Функция должна возвращать транспонированную матрицу matrix.

# def transpose(matrix):
#     return list(map(list, zip(*matrix)))

####################################################
# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#
# data — список произвольных объектов, сравнимых между собой
# Функция должна возвращать кортеж, в котором первым элементом является индекс
# минимального элемента в списке data, вторым — индекс максимального элемента в
# списке data. Если список data пуст, функция должна вернуть значение None.

# def get_min_max(data):
#     if not data:
#         return None
#     a = lambda x: x[1]
#     mx, _ = max(enumerate(data), key=a)
#     mn, _ = min(enumerate(data), key=a)
#     return mn, mx

#####################################################
# Реализуйте функцию starmap() с использованием функции map(), которая принимает два аргумента:
#
# func — функция
# iterable — итерируемый объект, элементами которого являются коллекции
# Функция starmap() должна работать аналогично функции map(), то есть возвращать итератор, элементами
# которого являются элементы итерируемого объекта iterable, к которым была применена функция func,
# с единственным отличием: func должна принимать не один аргумент — коллекцию (элемент iterable),
# а каждый элемент этой коллекции в качестве самостоятельного аргумента.

# def starmap(func, iterable):
#     return iter(func(*i) for i in iterable)



####################################################
# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементы которого сравнимы между собой
# Функция должна возвращать кортеж, в котором первым элементом является
# минимальный элемент итерируемого объекта iterable, вторым — максимальный
# элемент итерируемого объекта iterable. Если итерируемый объект iterable
# пуст, функция должна вернуть значение None

# def get_min_max(iterable):
#     mn = None
#     mx = None
#     for i in iterable:
#         if mn is None or i < mn: mn = i
#         if mx is None or i > mx: mx = i
#     return None if mn is None else (mn, mx)

####################################################
# Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор,
# бесконечно генерирующий единственное значение — строку i love beegeek!.
# infinite_love = iter(lambda: 'i love beegeek', '')

####################################################
# Реализуйте функцию is_iterable(), которая принимает один аргумент:
#
# obj — произвольный объект
# Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

# def is_iterable(obj):
#     return '__iter__' in dir(obj)

####################################################
# Реализуйте функцию is_iterator(), которая принимает один аргумент:
# obj — произвольный объект
# Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
# def is_iterator(obj):
#     return '__next__' in dir(obj)



####################################################
# Реализуйте функцию random_numbers(), которая принимает два аргумента:
#
# left — целое число
# right — целое число
# Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел
# в диапазоне от left до right включительно.

# from random import randint
# def random_numbers(left, right):
#     return iter(lambda: randint(left, right), right+1)



####################################################
# Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:
#
# obj — произвольный объект
# Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.

# class Repeater:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self.obj
#         return value


####################################################
# Реализуйте класс BoundedRepeater, порождающий итераторы, конструктор которого принимает два аргумента в следующем порядке:
    # obj — произвольный объект
    # times — натуральное число
# Итератор класса BoundedRepeater должен генерировать значение obj times раз, а затем возбуждать исключение StopIteration.

# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.times <= 0:
#             raise StopIteration
#         else:
#             self.times -= 1
#             value = self.obj
#             return value


####################################################
# Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:
#
# n — натуральное число,
# Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых я
# вляется квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.

# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.start = 0
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.n:
#             raise StopIteration
#         else:
#             self.start += 1
#             return self.start ** 2



####################################################
# Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.
# Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1

# class Fibonacci:
#     def __init__(self):
#         self.f1 = 1
#         self.f2 = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = self.f1
#         self.f1, self.f2 = self.f2, self.f2 + self.f1
#         return result



####################################################
# Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:
# number — ненулевое число
# Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных
# степеней числа number в порядке возрастания, начиная с нулевой степени.

# class PowerOf:
#     def __init__(self, number: int) -> None:
#         self.number = number
#         self.power = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.power += 1
#         return self.number ** self.power


####################################################
# Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:
# data — словарь
# Итератор класса DictItemsIterator должен генерировать последовательность кортежей, представляющих собой
# пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.


# class DictItemsIterator:
#     def __init__(self, data: dict) -> None:
#         self.data = data
#         self.data_iter = data.__iter__()
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         k =next(self.data_iter)
#         return (k, self.data[k])



####################################################
# Реализуйте класс CardDeck, порождающий итераторы, конструктор которого не принимает никаких аргументов.
#
# Итератор класса CardDeck должен генерировать последовательность из
# 52 игральных карт, а после возбуждать исключение StopIteration. Каждая карта должна представлять собой строку в следующем формате:
# <номинал> <масть>
# Например, 7 пик, валет треф, дама бубен, король червей, туз пик.
# class CardDeck:
#     def __init__(self):
#         self.nominee =  ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
#         self.index_nominee = 0
#         self.mast = ['пик', 'треф', 'бубен', 'червей']
#         self.index_mast = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index_mast > 3:
#             raise StopIteration
#         res = f'{self.nominee[self.index_nominee]} {self.mast[self.index_mast]}'
#         if self.index_nominee < 12:
#             self.index_nominee += 1
#         else:
#             self.index_mast += 1
#             self.index_nominee = 0
#         return res

####################################################
# Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:
# iterable — итерируемый объект
# Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.

# class Cycle:
#     def __init__(self,iterable):
#         self.iterable = iterable
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.iterable) - 1:
#             self.index = 0
#         else:
#             self.index += 1
#         return self.iterable[self.index]

####################################################
# Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
#
# left — целое число
# right — целое число
# n — натуральное число
# Итератор класса RandomNumbers должен генерировать последовательность из n
# случайных чисел от left до right включительно, а затем возбуждать исключение StopIteration.
# from random import randint
# class RandomNumbers:
#     def __init__(self, left:int, right:int, n:int) -> None:
#         self.left = left
#         self.right = right
#         self.n = n
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter == self.n:
#             raise StopIteration
#         self.counter += 1
#         return randint(self.left, self.right)






# Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
#
# language — код языка: ru — русский, en — английский
# Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:
#
# русского алфавита, если language имеет значение ru
# английского алфавита, если language имеет значение en

# class Alphabet:
#     def __init__(self, language:str):
#         self.start = ord('a') if language == 'en' else ord('а')
#         self.end = ord('z') if language == 'en' else ord('я')
#         self.n = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         res = chr(self.n)
#         if self.n == self.end:
#             self.n = self.start - 1
#         self.n += 1
#         return res


# Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
#
# start — целое или вещественное число
# end — целое или вещественное число
# step — целое или вещественное число, по умолчанию имеет значение 1
# Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end,
# включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.

# class Xrange:
#     def __init__(self, start:int, end:int, step:int = 1):
#         self.start = start
#         self.end = end
#         self.step = step
#         self.flag = step == abs(step)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         res = self.start
#         if self.flag:
#             if self.start >= self.end:
#                 raise StopIteration
#             self.start += self.step
#         else:
#             if self.start <= self.end:
#                 raise StopIteration
#             self.start += self.step
#
#         return res




