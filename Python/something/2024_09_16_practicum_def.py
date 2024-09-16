# 1. Перепишите решение следующей задачи с использованием функции. У нас есть две
# логические переменные: isWeekday, isVacation (выходной день и каникулы). Они могут
# принимать разные значения, всего 4 комбинации: true - true, true - false, false - false, false -
# true. Есть правило: мы можем поспать, если день не рабочий или мы на каникулах.
# Напишите программу, которая в зависимости от значений двух переменных печатает,
# можем ли мы поспать или нет. То есть для значений isWeekday = False и isVacation = False
# программа должна печатать “можете поспать”.
# ???? что с условием

def isSleep(*, isWeekday:bool, isVacation:bool) ->bool:
    print('You can sleep' if any((not isWeekday, isVacation))  else 'Get up!')

isSleep(isWeekday=True, isVacation=False)

# --------------------------------------
# Напишите функцию, которая возвращает факториал заданного числа.
# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!. Пользоваться математической
# библиотекой math в этой задаче запрещено. Во всех задачах считывайте входные
# данные через input() и выводите ответ через print().

# def make_factorial(*, num:int) ->int:
#     res = 1
#     for i in range(1, num+1):
#         res *= i
#     return res
#
# print(make_factorial(num=10))

# --------------------------------------
# Создайте текстовый файл persons.txt, где 5 строчек, в каждой фамилия;имя;возраст.
# То есть каждая строка - информация о человеке и данные разделены точкой с запятой.
# Напишите программу, которая вычитывает данные из файлы и печатает их на экран в формате
# Имя: <имя>, Фамилия <фамилия>, Возраст <возраст>.
# немного усложним


# import csv
# import sys
#
# with open('persons.csv', 'w', encoding='utf-8') as outfile:
#     file = [i.strip().split(';') for i in sys.stdin]
#     writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(['name', 'surname', 'age'])
#     writer.writerows(file)
#
# ------------------------
# with open('example.txt', 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         name, surname, age = line.strip().split()
#         print(f'name: {name}, surname: {surname}, age: {age}')



