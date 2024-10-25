# 1. Напишите генератор, который будет принимать на вход числа и возвращать их сумму.
# Генератор должен использовать инструкцию yield для возврата текущей суммы и должен
# продолжать принимать новые числа для добавления к сумме.
# Если генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму.
# Напишите программу, которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.

def gen_for_sum():
    sum = yield
    while True:
       sum += yield sum


result = gen_for_sum()
result.__next__()
while True:
    n = int(input())
    print('Sum is:', result.send(n))
    if n == 0:
        result.close()
        break



# 2. Напишите генератор, который будет генерировать арифметическую прогрессию

# def make_arithmetic_progression(start=1, step=1):
#     while True:
#         yield start
#         start += step
#
# res = make_arithmetic_progression(start=5, step=2)
# for _ in range(5):
#     print(next(res), end=' ')

# интересно, а мне бы зачли за решение эту строчку)))
# Это конечно не генератор, но работает аналогично
# from itertools import count


