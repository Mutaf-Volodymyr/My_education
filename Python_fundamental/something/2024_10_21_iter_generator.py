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



