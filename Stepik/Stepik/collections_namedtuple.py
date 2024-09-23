# Python содержит встроенный модуль collections, который содержит
# специализированные типы коллекций, альтернативных традиционным list, tuple, dict:
#     namedtuple
#     defaultdict
#     OrderedDict
#     Counter
#     ChainMap
#     deque
# В рамках данного урока мы изучим именованные кортежи (тип namedtuple).


# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])     # объявляем тип Point именованного кортежа
# point = Point(3, 7)                         # создаем именованный кортеж Point
# print(point)
# print(point.x, point.y)
# print(point[0], point[1])
# print(type(point))

# -------------------
# Функция namedtuple() выступает в роли фабричной функции, порождающей новые типы данных.
#
# Сигнатура данной функции имеет вид:
#
    # namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

# То есть функция принимает два обязательных параметра typename и field_names
# и три необязательных rename, defaults, module,
# имеющих значения по умолчанию False, None, None соответственно.


############# Параметр rename
# from collections import namedtuple
# headers = ('name', 'surname', 'age', 'class')
# Student = namedtuple('Student', headers, rename=True)
# stud = Student('Роман', 'Белых', 26, 10)
# print(stud)

############# Параметр defaults

# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'], defaults=(0, 0))
# point1 = Point()      # используем значения по умолчанию
# point2 = Point(1, 9)
#
# print(point1)
# print(point2)
#
# Можно указать значение по умолчанию только для некоторых полей, при этом
# defaults присваивает значения по умолчанию с конца.


############# Параметр module

# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'], module='customtypes')
# point = Point(1, 2)
# print(type(point))


############# атрибут _fields
#  содержит кортеж строк, в котором перечислены имена полей

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# tim = Person('Тимур', 29, 170)
# print(tim)
# print(tim._fields)
# print(Person._fields)


############# атрибут _field_defaults
# содержит словарь, который сопоставляет имена полей
# с соответствующими значениями по умолчанию, если таковые имеются.

############# Метод  _make()
# используется для создания именованных кортежей из итерируемых объектов
# (список, кортеж, строка, словарь и т.д.).

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person._make(['Timur', 29, 170])
# print(timur)



############# Метод _asdict()
# может преобразовывать именованные кортежи в словари

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person._make(['Timur', 29, 170])
# print(timur._asdict())

############# Метод  _replace()
# позволяет создавать новые именованные кортежи на основании
# уже существующих с заменой некоторых значений.

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'country'])
# timur1 = Person('Тимур', 29, 170, 'Russia')
# timur2 = timur1._replace(age=30, country='Germany')
# print(timur1)
# print(timur2)








############## ЗАДАЧИ #####################

# Дополните приведенный ниже код, чтобы он создал именованный кортеж
# Fruit с полями name, color и vitamins.
#
# from collections import namedtuple
# Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])


# -------------------------------------
# Вам доступен именованный кортеж Game. Дополните приведенный ниже код, чтобы
# он создал именованный кортеж типа ExtendedGame, имеющий те же поля, что и Game,
# а также два дополнительных поля — release_date и price.

# from collections import namedtuple
# Game = namedtuple('Game', 'name developer publisher')
# ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])