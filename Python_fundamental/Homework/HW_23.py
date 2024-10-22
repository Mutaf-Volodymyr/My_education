# 1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с
# использованием генераторного выражения. Реализуйте функцию generate_squares,
# которая принимает число N в качестве аргумента и использует генераторное
# выражение для генерации квадратов чисел. Затем выведите квадраты чисел на экран.


def generate_squares(n):
    if not isinstance(n, int) or n < 2:
        raise ValueError('n must be greater than 1 and integer type')
    yield from (i**2 for i in range(1, n+1))

res = generate_squares(10)
for i, q in enumerate(res, 1):
    print(f'Квадрат числа {i} = {q}')


# 2. Напишите генератор, который будет генерировать бесконечную последовательность Фибоначчи.
# Каждый раз, когда генератор вызывается, он должен возвращать следующее число последовательности.
# Напишите программу, которая будет использовать этот генератор для вывода первых N чисел Фибоначчи.

# УСЛОЖНИМ ЗАДАЧУ

# итератор Фибоначчи
class Fibonacci:
    def __init__(self):
        self.f1 = 1
        self.f2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.f1
        self.f1, self.f2 = self.f2, self.f2 + self.f1
        return result

# генератор Фибоначчи
def fibonacci():
    f1, f2 = 1, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

# функция, которая печатает заданное количество чисел последовательности,
# позволяя выбирать при помощи чего эта последовательность будет сгенерирована
def print_fib(n=5, use_gen_not_iter=True):
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be greater than 0 and integer type')
    if use_gen_not_iter:
        fib = fibonacci()
        print('Use generator: ', end='')
    else:
        fib = Fibonacci()
        print('Use iterator : ', end='')
    for _ in range(n):
        print(next(fib), end=' ')

# вызов функции
print_fib(10, use_gen_not_iter=False)
print()
print_fib(10, use_gen_not_iter=True)

