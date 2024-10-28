
# Вам доступна программа, которая находит сумму всех значений по ключу
# Likes из всех словарей списка blog_posts. Если словарь не содержит ключа Likes,
# его значение считается равным минус единице. Дополните приведенный ниже код конструкцией
# try-except, чтобы он выполнился без ошибок.


# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
# total_likes = 0
# for post in blog_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         total_likes -= 1
# print(total_likes)

###############################################################
# Вам доступна программа, которая добавляет в список fifth пятую букву каждого
# слова из списка food. Если слово не имеет пятой буквы, этой буквой считается
# символ _. Дополните приведенный ниже код конструкцией try-except, чтобы он выполнился без ошибок.
# food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
# fifth = []
#
# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError:
#         fifth.append('_')
# print(fifth)


###############################################################
# Вам доступна программа, которая добавляет в список remainders остаток от деления
# 36 на каждое число из списка numbers. Если число равно нулю, оно игнорируется.
# Дополните приведенный ниже код конструкцией try-except, чтобы он выполнился без ошибок.

# numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
# remainders = []
#
# for number in numbers:
#     try:
#         remainders.append(36 % number)
#     except ZeroDivisionError:
#         pass
#
# print(remainders)

###############################################################
# На вход программе подается неопределенное количество строк, каждая из которых
# содержит произвольное значение. Напишите программу с использованием конструкции
# try-except, которая выводит сумму всех введенных чисел, а затем —
# количество введенных нечисловых значений.

# from sys import stdin
# total = 0
# count = 0
# for num in stdin:
#     try:
#         total += float(num)
#     except ValueError:
#         count += 1
#
# print(int(total) if int(total) == total else total)
# print(count)



###############################################################
# Напишите программу с использованием конструкции try-except, которая выводит название месяца,
# соответствующее введенному целому числу (от 1 до 12 включительно), причем если введенное число не принадлежит отрезку
# [1;12], программа должна вывести текст:
# Введено число из недопустимого диапазона
# если введенное значение не является целым числом, программа должна вывести текст:
# Введено некорректное значение

# import calendar
# months = dict(zip(list(range(1, 13)), list(calendar.month_name)[1:]))
# try:
#     m = int(input())
#     try:
#         print(months[m])
#     except KeyError:
#         print('Введено число из недопустимого диапазона')
# except ValueError:
#     print("Введено некорректное значение")


###############################################################
# Реализуйте функцию add_to_list_in_dict() с использованием конструкции try-except, которая принимает три аргумента в следующем порядке:
    # data — словарь списков, то есть словарь, значениями в котором являются списки
    # key — хешируемый объект
    # element — произвольный объект
# Функция должна добавлять объект element в список по ключу key в словаре data. Если ключа key в словаре data нет,
# функция должна добавить его в словарь, присвоить ему в качестве значения пустой список и добавить в этот список объект element.

# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key].append(element)
#     except KeyError:
#         data[key] = [element]


###############################################################
# Напишите программу с использованием конструкции try-except, которая принимает
# на вход название текстового файла и выводит его содержимое. Если файла
# с данным названием нет в папке с программой, программа должна вывести текст:
# Файл не найден


# try:
#     with open(input(), 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('Файл не найден')

###############################################################


# Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
# number — целое число (от 1 до 7 включительно)
# Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
# если number не является целым числом, функция должна возбуждать исключение:
# TypeError('Аргумент не является целым числом')
# если number является целым числом, но не принадлежит отрезку
# [1;7], функция должна возбуждать исключение:
# ValueError('Аргумент не принадлежит требуемому диапазону')

#
# def get_weekday(number):
#     week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье", }
#     if not isinstance(number, int):
#         raise TypeError('Аргумент не является целым числом')
#     elif number not in week.keys():
#         raise ValueError('Аргумент не принадлежит требуемому диапазону')
#     else:
#         return week[number]




# Реализуйте функцию get_id(), которая принимает два аргумента:
#
# names — список имен учеников, обучающихся в школе
# name — имя поступающего ученика
# Функция должна возвращать идентификационный номер, который получит поступающий в школу ученик, при этом
#
# если имя ученика name не является строкой (тип str), функция должна возбуждать исключение:
# TypeError('Имя не является строкой')
# если имя ученика name является строкой (тип str), но не представляет собой корректное имя, функция должна возбуждать исключение:
# ValueError('Имя не является корректным')

# def get_id(names, name):
#     if not isinstance(name, str):
#         raise TypeError('Имя не является строкой')
#     elif not name.isalpha() or name != name.title():
#         raise ValueError('Имя не является корректным')
#     else:
#         return len(names) + 1



#
# Напишите программу, которая принимает на вход название JSON файла, десериализует содержащийся в этом файле объект и выводит его.
#
# если файла с данным названием нет в папке с программой, программа должна вывести текст:
# Файл не найден
# если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие формату JSON), программа должна вывести текст:
# Ошибка при десериализации

# import json
# try:
#     with open(input()) as file:
#         data = json.load(file)                # передаем файловый объект
#         print(data)
# except FileNotFoundError:
#     print("Файл не найден")
# except json.decoder.JSONDecodeError:
#     print('Ошибка при десериализации')


# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.

# def is_good_password(string):
#     if string != string.upper() and string != string.lower():
#         if any(i.isdigit() for i in string) and len(string) > 8:
#             return True
#     return False

# Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:
# LengthError, если его длина меньше  9 символов
# LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры

# class PasswordError(Exception):
#     pass
#
# class LengthError(PasswordError):
#     pass
#
# class LetterError(PasswordError):
#     pass
#
# class DigitError(PasswordError):
#     pass
#
#
# def is_good_password(string):
#     if len(string) < 9:
#         raise LengthError
#     elif string == string.upper() or string == string.lower():
#         raise LetterError
#     elif not any(i.isdigit() for i in string):
#         raise DigitError
#     else:
#         return True
#
#
# while True:
#     try:
#         is_good_password(input())
#     except LengthError:
#         print('LengthError')
#     except LetterError:
#         print('LetterError')
#     except DigitError:
#         print('DigitError')
#     else:
#         print('Success!')
#         break


