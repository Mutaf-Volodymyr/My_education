# ### Задача 2: Генератор простых чисел
#
# # Напишите генератор, который генерирует простые числа до `n`.
#
#
# from math import sqrt
# # einfach_numm = int(input())
#
# def einfach_gen(n):
#     yield 2
#     yield 5
#     for i in range(7, n + 1, 2):
#         p = int((sqrt(i)) + 1)
#         if i % 10 == 5:
#             continue
#         for j in (3, n):
#             if i % j == 0:
#                 break
#             if j > p:
#                 yield i
#
#
# res = einfach_gen(3000)
# for _ in range(3000):
#     print(next(res), end=', ')


# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
# 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
# 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, …

# from itertools import count, filterfalse
# is_prime = filterfalse(lambda x: not all(x % i for i in range(2, x)) , count(1, 2))
# for _ in range(20):
#     print(next(is_prime))

#################################

# def my_generator():
#     try:
#         print('11111')
#         yield 1
#         print('22222')
#         yield 2
#         yield 3
#     except ValueError:
#         print('++++')
#     yield from (i for i in range(20))
# #
# #
# #
# gen = my_generator()
# print(next(gen)) # Выводит 1
# gen.throw(ValueError("Enough"))
# print(next(gen))
# print(next(gen))
# print(next(gen))




# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))



# Напишите генератор, который принимает на вход поток элементов и выдает только уникальные
# элементы, сохраняя их порядок встречаемости (для уже повторяющихся элементов генератор
# не выдает ничего)

def my_generator():
    total_set = set()
    received_value = yield
    while True:
        if received_value not in total_set:
            total_set.add(received_value)
            received_value = yield received_value
        else:
            received_value = yield None

gen = my_generator()

gen.__next__()
while True:
    print(gen.send(int(input())))


