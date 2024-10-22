# Реализуйте функцию tabulate(), которая принимает один аргумент:
# func — произвольная функция
# Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность
# возвращаемых значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.
# from itertools import count
# def tabulate(func):
#     a = count(1)
#     yield from (func(i) for i in a)
import itertools


################################################
# Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность из n чисел,
# каждое из которых является факториалом очередного натурального числа.

# from itertools import accumulate
# import operator
#
# def factorials(n):
#     yield from accumulate(range(1, n+1), operator.mul)



################################################
# Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.
# Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных латинских букв

# from itertools import cycle
# from string import ascii_uppercase
#
# def alnum_sequence():
#     return cycle(el for t in zip(range(1, 27), ascii_uppercase) for el in t)


################################################
# Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов,
# каждый из которых является итерируемым объектом.
# Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных
# итерируемых объектов: сначала первый элемент первого итерируемого объекта, затем первый элемент
# второго итерируемого объекта, и так далее; после второй элемент первого итерируемого объекта,
# затем второй элемент второго итерируемого объекта, и так далее.

# from itertools import starmap, zip_longest
# def roundrobin(*args):
#     a = "TEST_9"
#     yield from (k for i in zip_longest(*args, fillvalue=a) for k in i if k != a)
#


#################################################
# Реализуйте функцию drop_while_negative(), которая принимает один аргумент:
#
    # iterable — итерируемый объект, элементами которого являются целые числа
# Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable,
# начиная с первого неотрицательного числа.

#
# from itertools import dropwhile
# def drop_while_negative(iterable):
#     return dropwhile(lambda x: x < 0, iterable)


#################################################
#
# Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:
    # iterable — итерируемый объект
    # obj — произвольный объект
# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта
# iterable, начиная с элемента, не равного obj.
#
# from itertools import dropwhile
# def drop_this(iterable, obj):
#     return dropwhile(lambda x: x == obj, iterable)



#################################################

# Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
# Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable,
# для которого функция predicate вернула значение True. Если такого элемента нет,
# функция first_true() должна вернуть значение None.


# def first_true(iterable, predicate):
#     return next(filter(predicate, iterable), None)



#################################################
# Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:
#
    # iterable — итерируемый объект
    # n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность из первых
# n элементов итерируемого объекта iterable.
# from itertools import islice
# def take(iterable, n):
#     return islice(iterable, n)


#################################################
# Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:
# iterable — итерируемый объект
# n — натуральное число
# Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable.
# Если итерируемый объект iterable содержит менее n элементов, функция должна вернуть значение None.

# from itertools import islice
# def take_nth(iterable, n):
#     return next(islice(iterable, n-1, n), None)


#################################################
# Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:
#
#     iterable — итерируемый объект, элементами которого являются целые числа
#     number — произвольное число
# Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number.
# Если таких элементов нет, функция должна вернуть число -1

# def first_largest(iterable, number):
#     res = next(filter(lambda n: n[1] > number, enumerate(iterable)), (-1, None))
#     return res[0]


#################################################

# Реализуйте функцию sum_of_digits(), которая принимает один аргумент:
# iterable — итерируемый объект, элементами которого являются натуральные числа
# Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.
#
# from itertools import chain
# def sum_of_digits(iterable):
#     return sum(map(int,chain.from_iterable(map(str, iterable))))


#################################################
# Реализуйте функцию is_rising(), которая принимает один аргумент:
# iterable — итерируемый объект, элементами которого являются числа
# Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию,
# или False в противном случае.
# from itertools import pairwise
# def is_rising(iterable):
#     return all(map(lambda x, y: x < y, pairwise(iterable)))


#################################################
# Реализуйте функцию max_pair(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются числа
# Функция должна возвращать единственное число — максимальную сумму двух соседних чисел итерируемого объекта iterable.

# from itertools import pairwise
# def max_pair(iterable):
#     return max(map(sum, pairwise(iterable)))





#################################################
# Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# times — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность элементов
# итерируемого объекта iterable, зацикленных times раз.

# from itertools import tee, chain
# def ncycles(iterable, times):
#     return chain.from_iterable(tee(iterable, times))



#################################################
# Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:
#
    # iterable — итерируемый объект
    # n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность,
# элементами которой являются объединенные в кортежи по n элементов
# соседние элементы итерируемого объекта iterable. Если у элемента
# не достаточно соседей, то ими становится значение None.
#
# from itertools import zip_longest
# def grouper(iterable, n):
#     args = [iter(iterable)] * n
#     return zip_longest(*args)



#################################################
# Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым элементом именованного кортежа
# является имя человека, вторым — возраст, третьим — рост. Также доступен список persons, содержащий эти кортежи.
#
# Дополните приведенный ниже код, чтобы он сгруппировал людей из данного списка по их росту и вывел полученные группы.
# Для каждой группы сначала должен быть указан рост, а затем через запятую перечислены имена людей, имеющих соответствующий рост.
# Группы должны быть расположены в порядке увеличения роста, каждая на отдельной строке, имена в группах — в алфавитном порядке,
# в следующем формате:


# from collections import namedtuple
# from itertools import groupby
#
# Person = namedtuple('Person', ['name', 'age', 'height'])
#
# persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
#            Person('Mark', 71, 172), Person('Alex', 45, 193),
#            Person('Jeff', 63, 193), Person('Ryan', 41, 184),
#            Person('Ariana', 28, 158), Person('Liam', 69, 193)]
#
# res = groupby(sorted(persons, key=lambda x: x.height), lambda x: x.height)
# for k, v in res:
#     print(str(k) + ':', ', '.join(sorted([i.name for i in v])))




#################################################
# Вам доступен именованный кортеж Student, который содержит данные об ученике.
# Первым элементом именованного кортежа является фамилия ученика, вторым — имя, третьим — класс.
# Также доступен список students, содержащий эти кортежи.
# Дополните приведенный ниже код, чтобы он вывел наиболее часто
# встречаемое имя среди учеников из данного списка.

# from collections import namedtuple
# from itertools import groupby
# Student = namedtuple('Student', ['surname', 'name', 'grade'])
# students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
#             Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
#             Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
#             Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
#             Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
#             Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
#             Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
#             Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
#             Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]
#
# group_iter = groupby(sorted(students), key=lambda student: student.name)
# print(max(group_iter, key=lambda tpl: sum(1 for i in tpl[1]))[0])


#################################################
# Напишите программу, которая группирует слова по их длине.
# from itertools import groupby
#
# a = sorted(input().split(), key=len)
# for k, v in groupby(a, len):
#     print(f'{k} -> ', end='')
#     print(*sorted(v), sep=', ')



from itertools import combinations

numbers1 = [1, 2, 3]
numbers2 = [3, 2, 1]

combinations1 = set(combinations(numbers1, 2))
combinations2 = set(combinations(numbers2, 2))

print(combinations1, combinations2)


