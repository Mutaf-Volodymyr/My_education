# Напишите программу, которая принимает матрицу (вложенный список) от пользователя
# и находит сумму всех элементов в матрице. Используйте вложенные списки и циклы для обхода элементов матрицы.

def make_empty_matrix() ->list:
    print('давайте создадим матрицу')
    m = is_valid_num('Введите ширину ')
    n = is_valid_num('Введите высоту ')
    return [[0]*m for i in range(n)]

def is_valid_num(a:str):
    while True:
        n = input(a)
        if n.isnumeric():
            return int(n)
        else:
            print('Введено недопустимое значение')

def filling_make_empty_matrix(matrix:list)->list:
    print('сейчас мы будем заполнять матрицу.')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = is_valid_num('Введите число ')
    print('Отлично! Матрица сформирована. Она выглядит так')
    for row in matrix:
        print(*row)
    return matrix


def make_sum_matrix(matrix:list) ->str:
    summ =[]
    for row in matrix:
        summ.append(sum(row))
    return f'Сумма чисел матрицы {sum(summ)}'


# print(make_sum_matrix(filling_make_empty_matrix(make_empty_matrix())))



# 2. Напишите программу, которая принимает список чисел от пользователя и сортирует его в порядке убывания,
# используя метод sort() и параметр reverse=True. Выведите отсортированный список на экран.

print(*sorted([is_valid_num('Введите число: ') for i in range(is_valid_num('Введите количество чисел: '))], reverse=True))