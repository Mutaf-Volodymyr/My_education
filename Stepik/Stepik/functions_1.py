#
###########################################
#
# def convert(number):
#     return tuple([v(number).replace(k, '').upper() for k, v in {'0b':bin, '0o':oct, '0x':hex}.items()])
#
# print(convert(15))


###########################################
# Как уже известно, функция zip() объединяет элементы различных последовательностей.
# Особенностью функции является то, что при передаче последовательностей различной длины
# элементы последовательности большей длины будут отброшены.
# Реализуйте функцию zip_longest(), которая принимает переменное количество
# позиционных аргументов, каждый из которых является списком,
# и один необязательный именованный аргумент fill, имеющий значение по умолчанию None.
# Функция должна объединять элементы переданных последовательностей в кортежи, аналогично функции zip(),
# и возвращать в виде списка, но если последовательности имеют различную длину,
# недостающие элементы последовательностей меньшей длины должны принимать значение fill.

# def zip_longest(*args:list, fill=None):
#     args = sorted(args, key=len, reverse=True)
#     mx = len(args[0])
#     for i in range(1, len(args)):
#         l = len(args[i])
#         if l < mx:
#             args[i].extend([fill]*(mx-l))
#     return list(zip(*args))

#################################
# code = '''
# def get_smiley_face():
#     return "=(^~^)="
#
# print(get_smiley_face())'''
#
# exec(code)


#################################

# input_any_type = eval(input())
#
# match input_any_type:
#     case list():
#         print(input_any_type[-1])
#     case tuple():
#         print(input_any_type[0])
#     case set():
#         print(len(input_any_type))


#################################
# f = input()
# a, b = map(int, input().split())
# l = [eval(f) for x in range(a,b+1)]
# print(f'Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(l)}')
# print(f'Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(l)}')

# 2*x**2 + 5*x + 7
# -1 5

################################
# def hash_as_key(a):
#     res = dict()
#     for i in a:
#         res[hash(i)] = res.get(hash(i), []) + [i]
#     for k, v in res.items():
#         if len(v) == 1:
#             res[k] = v[0]
#     return res
#
# data = [1, 2, 3, 4, 5, 5]
#
# print(hash_as_key(data))
###########################################
# Вам доступен список data, содержащий произвольные объекты. Дополните приведенный ниже код,
# чтобы он вывел все числа (тип int и float), находящиеся в данном списке, отбрасывая
# дробную часть у вещественных чисел. Числа должны быть расположены в своем исходном порядке, каждое на отдельной строке.

# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546,
#         976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621,
#         -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '',
#         323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number',
#         104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
#
#
# print(*map(int, filter(lambda x: type(x) in (int, float), data)), sep='\n')

###########################################
# Вам доступен список numbers, содержащий целые числа. Дополните приведенный ниже код, чтобы он вывел сумму
# квадратов всех двузначных чисел из данного списка, которые делятся на 9 без остатка.

# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623,
#            -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982,
#            1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808,
#            -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378,
#            -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558,
#            1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148,
#            4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]

# print(sum(map(lambda x: x**2, filter(lambda x: x%9 == 0 and -100<x<100, numbers))))

###########################################
# Вам доступен список names, содержащий имена на русском языке. Дополните приведенный ниже код,
# чтобы он вывел все имена, которые начинаются на буквы А и М (независимо от регистра) и имеют длину больше 4
# Имена должны быть расположены в лексикографическом порядке, через пробел, каждое с заглавной буквы.

# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита',
#          'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём',
#          'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия',
#          'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр',
#          'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей',
#          'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина',
#          'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен',
#          'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур',
#          'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
#
# print(*sorted(filter(lambda x: x[0] in ('А', 'М') and len(x)>4, map(str.title, names))))

###########################################
# Используя синтаксис анонимных функций, реализуйте рекурсивную функцию fib(), которая принимает один аргумент:
# n — натуральное число
# Функция должна возвращать n-ый член последовательности Фибоначчи.

# fib = lambda x: 1 if x <= 2 else fib(x-1) + fib(x-2)
# print(fib(6))

###########################################
# Реализуйте функцию print_operation_table(), которая принимает три аргумента в следующем порядке:
#
# operation — функция, характеризующая некоторую бинарную операцию
# rows — натуральное число
# cols — натуральное число
# Функция должна составлять и выводить таблицу из rows строк и cols столбцов, в которой элемент со строкой
# n и столбцом m имеет значение operation(n, m).

# def print_operation_table(operation, rows:int, cols:int):
#     matrix = [[1]*cols for _ in range(rows)]
#     for i in range(rows):
#         for j in range(cols):
#             matrix[i][j] = operation(i+1, j+1)
#     for r in matrix:
#         print(*r)
#
#
# print_operation_table(lambda a, b: a * b, 5, 5)
#
# print_operation_table(pow, 5, 4)

###########################################
# Реализуйте функцию numbers_sum(), которая принимает один аргумент:
# elems — список произвольных объектов
# Функция должна возвращать сумму чисел (типы int и float), находящихся в списке elems,
# игнорируя все нечисловые объекты. Если в списке elems нет чисел, функция должна вернуть число 0

# def numbers_sum(elems):
#     '''Принимает список и возвращает сумму его чисел (int, float), \nигнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
#     res = []
#     for elem in elems:
#         match elem:
#             case int()  : res.append(elem)
#             case float(): res.append(elem)
#     return sum(res)
#
# print(numbers_sum.__doc__,)

###########################################

# Реализуйте функцию polynom(), которая принимает один аргумент:
#
# x — вещественное число
# Функция должна возвращать значение выражения x ** 2  + 1.

# Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции, которые уже были вычислены.

# def polynom(x):
#     res = x**2 + 1
#     polynom.__dict__.setdefault('values', set()).add(res)
#     return res


###########################################
# Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:
    # text — произвольная строка
    # marks — набор символов
# Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.
# Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.

# def remove_marks(text, marks):
#     remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1
#     for i in marks:
#         text = text.replace(i, "")
#     return text

################### АХУЕТЬ ########################

# def closure():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     return inner
#
# start = closure()
# another = closure()             # другое замыкание, со своими локальными значениями
#
# start()                         # выводит 1
# start()                         # выводит 2
#
# another()                       # выводит 1
#
# start()                         # выводит 3


###########################################
# Реализуйте функцию power(), которая принимает один аргумент:
# degree — целое число
# Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x
# и возвращает значение x в степени degree.

# def power(degree):
#     def inner(x):
#         return x ** degree
#     return inner

###########################################
# Реализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:
    # a — вещественное число, коэффициент
    # b — вещественное число, коэффициент
    # c — вещественное число, коэффициент
# Функция generator_square_polynom() должна возвращать функцию, которая принимает в качестве аргумента
# вещественное число x и возвращает значение выражения квадратного трехчлена.

# def generator_square_polynom(a, b, c):
#     return lambda x: a*x*x + b*x + c


###########################################
# Реализуйте функцию sourcetemplate(), которая принимает один аргумент:
# url — URL адрес
# Функция sourcetemplate() должна возвращать функцию, которая принимает
# произвольное количество именованных аргументов и возвращает url адрес,
# объединенный со строкой запроса, сформированной из переданных аргументов.
# При вызове без аргументов она должна возвращать исходный url адрес без изменений.

# def sourcetemplate(url):
#     def inner(**kwargs):
#         res = '&'.join((str(k)+'='+str(v) for k, v in sorted(kwargs.items())))
#         return url + '?' + res if res else url
#     return inner
#
# url = 'https://beegeek.ru'
# load = sourcetemplate(url)
# print(load())




###########################################
# Реализуйте функцию date_formatter(), которая принимает один аргумент:
#
# country_code — код страны
# Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date)
# и возвращает строку с данной датой в формате страны с кодом country_code.

# from datetime import date
# def date_formatter(country_code):
#     def inner(d):
#         match country_code:
#             case 'ru': p = '%d.%m.%Y'
#             case 'us': p = '%m-%d-%Y'
#             case 'ca': p = '%Y-%m-%d'
#             case 'br': p = '%d/%m/%Y'
#             case 'fr': p = '%d.%m.%Y'
#             case 'pt': p = '%d-%m-%Y'
#         return d.strftime(p)
#     return inner
#
# date_ru = date_formatter('ru')
# today = date(2022, 1, 25)
# print(date_ru(today))



###########################################
# Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
# values — список чисел
# group — список, кортеж или множество чисел
# Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной
# группу чисел из group, которая должна следовать первой.

# def sort_priority(values, group):
#     values[:] = sorted([(0 if i in group else 1, i) for i in values])
#     values[:] = [j for _, j in values]

