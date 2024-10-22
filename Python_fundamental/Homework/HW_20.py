# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей в качестве аргументов и возвращает
# новый словарь, объединяющий все входные словари. Если ключи повторяются, значения должны быть объединены в список.
# Функция должна использовать аргумент *args для принятия произвольного числа аргументов словаря.


# def merge_dicts(*args):
#     res_dict = {}
#     for d in args:
#         for k, v in d.items():
#             res_dict[k] = res_dict.get(k, []) + [v]
#     return res_dict
#
# print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}))
# # {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}



# 2. Напишите программу, которая принимает строку от пользователя и подсчитывает количество уникальных
# символов в этой строке. Создайте функцию count_unique_chars, которая принимает строку и возвращает количество
# уникальных символов. Выведите результат на экран.

# def count_unique_chars(string:str) ->dict[str, int]:
#     res_dict = {}
#     for char in string:
#         res_dict[char] = res_dict.get(char, 0) + 1
#     return res_dict
#
# print(count_unique_chars('hello'))
#
# # или можно не придумывать велосипед
# from collections import Counter
# print(dict(Counter("-Say my name! -Heisenberg... -You're goddamn right!")))




# 3. Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках.
# Ключами словаря являются имена студентов, а значениями - списки оценок. Создайте функцию calculate_average_grade,
# которая принимает словарь с оценками студентов и вычисляет средний балл для каждого студента.
# Функция должна возвращать новый словарь, в котором ключами являются имена студентов,
# а значениями - их средний балл. Выведите результат на экран.


# def make_dict_students() ->dict[str, list[int]]:
#     res_dict = dict()
#     for i in range(int(input('Введите количество студентов: '))):
#         key = input(f'Как зовут студента №{i+1}? ').title()
#         value = [int(n) for n in input('Введите его оценки через пробел: ').split()]
#         res_dict[key] = value
#     return res_dict
#
#
# def calculate_average_grade(student:dict[str, list]) -> dict[str, float]:
#     return {k: round(sum(v)/len(v), 2) for k, v in student.items()}
#
# grades = {
#     'Alice': [85, 90, 92],
#     'Bob': [78, 80, 84],
#     'Carol': [92, 88, 95]
# }

# print(calculate_average_grade(grades))
# print(calculate_average_grade(make_dict_students()))

