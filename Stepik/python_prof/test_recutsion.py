# модель оказалась не рабочей

from time import perf_counter
from functools import lru_cache

@lru_cache
def factorial_cached(n: int) -> int:
    if n == 0:
        return 1
    return factorial(n - 1) * n

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def factorial_common(n):
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


range_num = 100





start = perf_counter()
for i in range(range_num):
    factorial_cached(i)
end = perf_counter()
fc = end-start
print(f'Время подсчета функции с мемоизацией: {round((fc), range_num)}')

start = perf_counter()
for i in range(range_num):
    factorial(i)
end = perf_counter()
f = end-start
print(f'Время подсчета функции без мемоизации: {round((f), range_num)}')

start = perf_counter()
for i in range(range_num):
    factorial_common(i)
end = perf_counter()
fs = end-start
print(f'Время подсчета функции с обычным циклом: {round((fs), range_num)}')

print()

print(f'Функция с мемоизацией работает быстрее обычной рекурсивной в {round(f/fc)} раз(-а)')
print(f'Функция с мемоизацией работает быстрее функции с обычным циклом в {round(fs/fc)} раз(-а)')