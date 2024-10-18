# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и
# выводит на экран наиболее часто встречающиеся слова. Для решения задачи используйте класс
# Counter из модуля collections. Создайте функцию count_words, которая принимает текст в качестве
# аргумента и возвращает словарь с количеством вхождений каждого слова. Выведите наиболее
# часто встречающиеся слова и их количество.

# from collections import Counter
# from string import punctuation
# def count_words(text):
#     text = [i.lower().strip(punctuation) for i in text.split()]
#     res = Counter(text)
#     return res
#
#
# for k, v in count_words(input()).items():
#     print(f'слово "{k}" встречается: {v} раз(а)')




# 2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке,
# включающий поля name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'city'], defaults=('NoName', 'NoAge', 'NoCity'))
#
# alice = Person('Alice', 25, 'New York')
# bob = Person('Bob', 30, 'London')
# carol = Person('Carol', 35)
# someone = Person()
#
# for i in [alice, bob, carol, someone]:
#     print(f'{i.name}s {i.age} years old.')


# 3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для указанного
# ключа с использованием метода get или setdefault. Создайте функцию get_value_from_dict, которая принимает словарь
# и ключ в качестве аргументов, и возвращает значение для указанного ключа, используя метод get или setdefault
# в зависимости от выбранного варианта. Выведите полученное значение на экран.
#

# def get_value_from_dict(di:dict, k:str|int, flag=True):
#     if flag:
#         return di.get(k, 'нет ключа')
#     else:
#         return di.setdefault(k, 'нет значения')
#
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# print(get_value_from_dict(my_dict, 'banana'))
# print(get_value_from_dict(my_dict, 'bananaAAAAA'))
# print(get_value_from_dict(my_dict, 'bananaAAAAA', False))
# print(my_dict)
