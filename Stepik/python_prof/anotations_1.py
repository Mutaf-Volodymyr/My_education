# Реализуйте функцию get_digits() c использованием аннотаций типов, которая принимает один аргумент:
#
# number — положительное целое или вещественное число
# Функция должна возвращать список, состоящий из цифр числа number.

# def get_digits(number: int| float) ->list[int]:
#     return [int(i) for i in list(str(number)) if i != '.']


# Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:
#
# grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список оценок по ключу grades
# Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.


# Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:
#
# grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список оценок по ключу grades
# Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.


# def top_grade(grades:dict[str, str | list[int]]) -> dict[str, str | int] :
#     res = {'name': grades['name'], 'top_grade': max(grades['grades'])}
#     return res
#
#
# info = {'name': 'Timur', 'grades': [30, 57, 99]}
#
# print(top_grade(info))
#
# print(*top_grade.__annotations__.values())




# Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:
#
# numbers — список целых или вещественных чисел
# step — целое число
# Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов,
# и возвращать значение None. Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
# from collections import deque
# def cyclic_shift(numbers:list[int | float], step:int) ->None:
#     temp = deque(numbers)
#     temp.rotate(step)
#     numbers[:] = [c for c in temp]
#
#
# print(*cyclic_shift.__annotations__.values())


#
# Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, которая принимает один аргумент:
#
# matrix — матрица произвольной размерности, элементами которой являются целые или вещественные числа
# Функция должна возвращать словарь, ключом в котором является номер строки матрицы, а значением — список элементов этой строки.


def matrix_to_dict(matrix:list[list[int | float]] ) ->dict[int, list[int | float]]:
    return {i: row for i, row in enumerate(matrix, 1)}


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))
