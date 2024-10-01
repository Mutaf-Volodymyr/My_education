# 1. Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list,
# которая изменяет элементы списка. Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
# Выведите измененный список на экран. Объясните, почему изменения происходят только внутри функции и как
# работают изменяемые и неизменяемые параметры.
# Пример вывода:
# Введите список чисел, разделенных пробелами: 1 2 3 4 5
# Измененный список чисел: [2, 1, 6, 2, 10]

# def modify_list(a:list) ->list:
#     ''' this function modifies a list whose elements are prime numbers according to the following rule
#         :an even number will be divided by two
#         :an odd number will be multiplied by two'''
#     return [int(i)*2 if int(i) % 2 else int(int(i)/2) for i in a]
#
# print(modify_list.__doc__)
# print(modify_list(input().split()))



# 2. Напишите программу, которая принимает произвольное количество аргументов
# от пользователя и передает их в функцию calculate_sum, которая возвращает сумму всех аргументов.
# Используйте оператор * при передаче аргументов в функцию. Выведите результат на экран.
# Пример вывода:
# Введите числа, разделенные пробелами: 1 2 3 4 5
# Сумма чисел: 15

# def calculate_sum(*args):
#     '''if at any point in your life you consider yourself
#     useless - think about this function!'''
#     return sum(args)

# a = (int(i) for i in input().split())
# print(calculate_sum(*a))
# print(calculate_sum.__doc__)

############ Казалось бы, зачем? Если можно сделать так:
# print(sum((int(i) for i in input().split())), '😎')

############ Или так:
# print(sum(map(int, input().split())), '😎')

############ Ну или вот так:
# from functools import reduce
# print(reduce(lambda x, y: int(x) + int(y), input().split(), 0), '😎')

############ Ну и конечно же, почему бы не сделать так:
# def recursive_sum(bdsm):
#     total = 0
#     for elem in bdsm:
#         if isinstance(elem, list):
#             total += recursive_sum(elem)
#         else:
#             total += elem
#     return total
#
# my_list = [12, [13, [53, 632], 6], [2342341, [98, 3123, [2432, [1, 1, 2, 3, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4]]]]]]]]], 4324]]]]
# print(recursive_sum(my_list), '😎')





