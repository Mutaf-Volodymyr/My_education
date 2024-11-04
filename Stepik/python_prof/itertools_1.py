# Реализуйте функцию tabulate(), которая принимает один аргумент:
# func — произвольная функция
# Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность
# возвращаемых значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.
# from itertools import count
# def tabulate(func):
#     a = count(1)
#     yield from (func(i) for i in a)
import string
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


# from itertools import combinations

# numbers1 = [1, 2, 3]
# numbers2 = [3, 2, 1]
#
# combinations1 = set(combinations(numbers1, 2))
# combinations2 = set(combinations(numbers2, 2))
#
# print(combinations1, combinations2)

# ополните приведенный ниже код, чтобы он вывел все дела Тимура в алфавитном порядке,
# указав для каждого набор соответствующих действий в правильной очередности, в следующем формате:


from itertools import groupby
# tasks = [('Отдых', 'поспать днем', 3),
#         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
#         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
#         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
#         ('Отдых', 'погулять вечером', 4),
#         ('Курс по ооп', 'обсудить темы', 1),
#         ('Урок по groupby', 'добавить задачи на программирование', 3),
#         ('Урок по groupby', 'написать конспект', 1),
#         ('Отдых', 'погулять днем', 2),
#         ('Урок по groupby', 'добавить тестовые задачи', 2),
#         ('Уборка', 'убраться в ванной', 2),
#         ('Уборка', 'убраться в комнате', 1),
#         ('Уборка', 'убраться на кухне', 3),
#         ('Отдых', 'погулять утром', 1),
#         ('Курс по ооп', 'обсудить задачи', 2)]

# f = lambda x: x[0]
# sort_tasks = sorted(tasks, key=f)
#
# for k, v in groupby(sort_tasks, key=f):
#     print(f'{k}:')
#     for _, task, num in sorted(v, key=lambda x: x[2]):
#         print(f'\t{num}. {task}')
#     print()


#
# Реализуйте функцию group_anagrams(), которая принимает один аргумент:
#
# words — список слов
# Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных кортежей.
#
# from itertools import groupby
# def group_anagrams(words:list[str])->list[tuple]:
#     l = lambda x: sorted(x)
#     return list(tuple(v) for _, v in groupby(sorted(words, key=l), l))
#
# groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
#
# print(*groups)


# Реализуйте функцию ranges(), которая принимает один аргумент:
#
# numbers — список различных натуральных чисел, расположенных в порядке возрастания
# Функция должна преобразовывать числа из списка numbers в отрезки, представляя их в виде кортежей,
# где первый элемент кортежа является левой границей отрезка, второй элемент — правой границей отрезка.
# Полученные кортежи-отрезки функция должна возвращать в виде списка.

# from itertools import groupby
# def ranges(numbers:list[int]) -> list[tuple]:
#     numbers = sorted(numbers, key=lambda x: numbers.index(x) - x)
#     res = []
#     for _, v in groupby(numbers, key=lambda x: numbers.index(x) - x):
#         v = list(v)
#         res.append((v[0], v[-1]))
#     return sorted(res)


# Напишите программу, которая выводит все перестановки символов строки без дубликатов.

# from itertools import permutations
#
# all_num_permutations = permutations(input())
# for i in sorted(set(all_num_permutations)):
#     print(''.join(i))


# Дополните приведенный ниже код, чтобы он вывел количество
# способов, которыми Тимур может приобрести книгу стоимостью 100$.

# from itertools import combinations
# wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
# counter = 0
# for i in range(1, 16):
#     for res in set(combinations(wallet, i)):
#         if sum(res) == 100:
#             counter += 1
# print(counter)


# from itertools import combinations_with_replacement
#
# wallet = [100, 50, 20, 10, 5]
# counter = 0
# for i in range(1, 21):
#     for res in set(combinations_with_replacement(wallet, i)):
#         if sum(res) == 100:
#             counter += 1
# print(counter)

# def gen_100():
#     for x1 in range(0, 101, 100):
#         for x2 in range(0, 101, 50):
#             for x3 in range(0, 101, 20):
#                 for x4 in range(0, 101, 10):
#                     for x5 in range(0, 101, 5):
#                         yield x1 + x2 + x3 + x4 + x5
#
# print(sum(1 for x in gen_100() if x == 100))


# from collections import namedtuple
# from functools import reduce
# import itertools
#
# Item = namedtuple('Item', ['name', 'mass', 'price'])
#
# items = [Item('Обручальное кольцо', 7, 49_000),
#          Item('Мобильный телефон', 200, 110_000),
#          Item('Ноутбук', 2000, 150_000),
#          Item('Ручка Паркер', 20, 37_000),
#          Item('Статуэтка Оскар', 4000, 28_000),
#          Item('Наушники', 150, 11_000),
#          Item('Гитара', 1500, 32_000),
#          Item('Золотая монета', 8, 140_000),
#          Item('Фотоаппарат', 720, 79_000),
#          Item('Лимитированные кроссовки', 300, 80_000)]
#
# winner = {}
# max_mass = int(input())
# for i in range(1, len(items)+1):
#     for res in itertools.combinations(items, i):
#         mass = reduce(lambda x, y: x + y.mass, res, 0)
#         if mass <= max_mass:
#             money = reduce(lambda x, y: x + y.price, res, 0)
#             winner[res] = money
#
#
# if winner:
#     for res in sorted(max(winner, key=lambda x: winner[x]), key=lambda x: x.name):
#         print(res.name)
# else:
#     print('Рюкзак собрать не удастся')

# Вам доступна программа, которая выводит все обозначения полей шахматной доски в алфавитном порядке через пробел.
#
# Перепишите данную программу с использованием функции product(), чтобы она выполняла ту же задачу.

# from string import ascii_lowercase
# from itertools import product
#
# letters = ascii_lowercase[:8]
# digits = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for a, b in product(letters, digits):
#     print(f'{a}{b}', end=' ')


# Вам доступна функция password_gen(), которая возвращает генератор, порождающий все трехсимвольные строковые пароли
# Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.

# from itertools import product
# def password_gen():
#     yield from map(lambda x: f'{x[0]}{x[1]}{x[2]}', (product(range(10), repeat=3)))




# Напишите программу, которая генерирует в системе счисления n все числа длины m

from itertools import product
yo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

n, m = int(input()), int(input())
for i in product(yo[0:n], repeat=m):
    print(''.join(i), end=' ')