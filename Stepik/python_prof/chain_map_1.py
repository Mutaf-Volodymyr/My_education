# Напишите программу, которая определяет, сколько всего животных обитает в зоопарке, и выводит полученный результат.

# from collections import ChainMap
# import json
# with open('ChainMap_1/zoo.json', 'r') as f:
#     file = json.load(f)
#     res = ChainMap(*file)
#     print(sum(res.values()))


# from collections import ChainMap, Counter
#
# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
#
# menu = ChainMap(bread, meat, sauce, vegetables, toppings)
# chek = Counter(input().split(','))
# l = len(max(chek, key=len))
# total = sum(menu[k] * v for k, v in chek.items())
# len_row = [len(f'ИТОГ: {str(total)}р')]
# for k, v in sorted(chek.items()):
#     row = f'{k.ljust(l)} x {v}'
#     len_row.append(len(row))
#     print(row)
# print('-'* max(len_row))
# print(f'ИТОГ: {total}р')



# Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap.
# Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.

# from collections import ChainMap
# def get_all_values(chainmap, key):
#     return {i.get(key) for i in chainmap.maps if i.get(key) != None}



# Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — хешируемый объект
# value — произвольный объект
# Функция должна изменять все значения по ключу key во всех словарях в chainmap на value.
# Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый словарь.

# from collections import ChainMap
# def deep_update(chainmapm, key, value):
#     flag = True
#     for di in chainmapm.maps:
#         if key in di:
#             di[key] = value
#             flag = False
#     if flag:
#         chainmapm[key] = value
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'age', 20)
#
# print(chainmap)



# Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# from_left — булево значение, по умолчанию равное True
# Функция должна возвращать значение по ключу key из chainmap, причем:
#
# если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
# если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому
# Если ключ key отсутствует в chainmap, функция должна вернуть значение None.
#
# from collections import ChainMap
# def get_value(chainmap, key, from_left=True):
#     if from_left:
#         for i in chainmap.maps:
#             if key in i:
#                 return i[key]
#     else:
#         for i in chainmap.maps[::-1]:
#             if key in i:
#                 return i[key]
#
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
#
# print(get_value(chainmap, 'age'))


