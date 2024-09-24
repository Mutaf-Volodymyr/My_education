# from collections import OrderedDict
#
# numbers = OrderedDict()
#
# numbers['one'] = 1
# numbers['two'] = 2
# numbers['three'] = 3
#
# print(numbers)

# OrderedDict словари имеют два полезных метода:
    # метод move_to_end() позволяет переместить существующий элемент либо в конец, либо в начало словаря
    # метод popitem() позволяет удалить и вернуть элемент либо из конца, либо из начала словаря

# Методу move_to_end() можно передать два аргумента:
    # key (обязательный аргумент) – ключ, который идентифицирует перемещаемый элемент
    # last (необязательный аргумент) – логическое значение (тип bool), которое определяет, в какой конец словаря мы перемещаем элемент, значение True (по умолчанию) перемещает элемент в конец, значение False – в начало

# С помощью метода move_to_end() мы можем сортировать OrderedDict словарь по ключам.
# from collections import OrderedDict
# letters = OrderedDict(b=2, d=4, a=1, c=3)
# for key in sorted(letters):
#     letters.move_to_end(key)
# print(letters)

# метод popitem() удаляет элементы с конца словаря.
# Если методу popitem() передать необязательный аргумент last=False, то он начнет удалять
# и возвращать элементы в порядке FIFO (First-In/First-Out, первый пришел/первый ушел).

################ ЗАДАЧИ #####################
# Вам доступен словарь data. Дополните приведенный ниже код, чтобы он вывел данный словарь,
# расположив его элементы в обратном порядке.



# from collections import OrderedDict
#
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
#                     'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
#                     'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
#                     'SeatsCount': '10'})
#
# for key in data.copy():
#     data.move_to_end(key, False)
# print(data)

# Вам доступен словарь data с четным количеством элементов. Дополните приведенный ниже код,
# чтобы он вывел данный словарь, расположив его элементы по следующему правилу:
# первый, последний, второй, предпоследний, третий, и так далее.

# from collections import OrderedDict
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
#                     'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
#                     'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
#                     'SeatsCount': '10'})
# res = []
# flag = False
# while data:
#      res.append(data.popitem(flag))
#      flag = not flag
#
# print(OrderedDict(res))

# Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:
    # ordered_dict — словарь OrderedDict
    # by_values — булево значение, по умолчанию имеет значение False
# Функция должна сортировать словарь ordered_dict:
    # по ключам, если by_values имеет значение False
    # по значениям, если by_values имеет значение True

from collections import OrderedDict
def custom_sort(ordered_dict, by_values=False):
    for i, _ in sorted(ordered_dict.items(), key=lambda t: t[1] if by_values else t[0]):
        ordered_dict.move_to_end(i, True)




data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
print(data)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())



