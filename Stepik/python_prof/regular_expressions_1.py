# Вам доступен набор телефонных номеров, имеющих следующие форматы:
#
# <код страны>-<код города>-<номер>
# <код страны> <код города> <номер>
# в котором код страны и код города представлены последовательностями от одной до трех цифр включительно,
# а номер — последовательностью от четырех до десяти цифр включительно. Между кодом страны, кодом города
# и номером используется разделитель, которым служит либо символ дефис, либо пробел, причем одновременно
# оба вида разделителя в одном номере присутствовать не могут.
#
# Напишите программу, которая принимает произвольное количество телефонных номеров и для каждого выводит
# отдельно его код страны, код города и номер.
from typing import re

# from re import fullmatch
# from sys import stdin
#
# regex = r'(?P<country>\d{1,3})( |-)(?P<city>\d{1,3})\2(?P<numer>\d{4,10})'
#
# res = [fullmatch(regex,tel_num.strip()).groupdict() for tel_num in stdin]
#
# for el in res:
#     print(f'Код страны: {el['country']}, Код города: {el['city']}, Номер: {el['numer']}')


######################################################
# В онлайн-школе BEEGEEK логин учетной записи определяется следующим образом:
#
# первым символом является символ нижнего подчеркивания _
# затем следуют одна или более цифр
# после записываются ноль или более латинских букв в произвольном регистре
# логин может иметь на конце необязательный символ нижнего подчеркивания _
# Напишите программу, которая принимает произвольное количество строк и определяет,
# какие из них представляют собой корректный логин онлайн-школы BEEGEEK.
#
# from re import fullmatch
# from sys import stdin
#
# regex = r'_\d+[A-Za-z]*_?'
#
# res = [bool(fullmatch(regex,login.strip())) for login in stdin]
# print(*res, sep='\n')

#######################################################
# Напишите программу, которая выводит слова, состоящие из двух одинаковых слогов.

# from re import fullmatch
# from sys import stdin
#
# regex = r'\b(\w+)\1\b'
#
# res = [fullmatch(regex,wort.strip()) for wort in stdin]
# for i in res:
#     if i:
#         print(i.group())


#######################################################
# Напишите программу, определяющую:
#
# количество строк, в которых bee встречается в качестве подстроки не менее двух раз
# количество строк, в которых geek встречается в качестве слова хотя бы один раз

# from re import search
# from sys import stdin
#
# regex_bee = r'bee.*bee'
# regex_geek = r'\bgeek\b'
#
# res = [(bool(search(regex_bee,wort.strip())), bool(search(regex_geek,wort.strip()))) for wort in stdin]
# res_1 = list(zip(*res))
#
# print(sum(res_1[0]), sum(res_1[1]), sep='\n')

#########################
# В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность.
# Для этого мы собираем публикации из различных соцсетей, которые содержат вхождения строки
# beegeek в нижнем регистре. Мы оцениваем публикацию:
# 3 балла, если она начинается и заканчивается строкой beegeek
# 2 балла, если она только начинается или только заканчивается строкой beegeek
# 1 балл, если она содержит строку beegeek только внутри
# 0 баллов, если она не содержит строку beegeek
# Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования
# баллов всех публикаций.

# from re import fullmatch, search
# from sys import stdin
#
# regex_3 = r'^(beegeek).*\1$'
# regex_2 = r'(^beegeek.*)|(.*beegeek$)'
# regex_1 = r'beegeek'
# total = 0
# for line in stdin:
#     line = line.strip()
#     if fullmatch(regex_3, line):
#         total += 3
#     elif fullmatch(regex_2, line):
#         total += 2
#     elif search(regex_1, line):
#         total += 1
#
# print(total)

#########################
# На электронную почту Тимура нередко приходят письма с предложением о сотрудничестве. Тимур ценит взаимное уважение и считает письмо достойным внимания, если оно начинается с одного из следующих выражений:
#
# Здравствуйте
# Доброе утро
# Добрый день
# Добрый вечер
# Напишите программу, которая определяет, является ли письмо достойным внимания Тимура.

# from re import IGNORECASE, search
# text = input()
# regex = r'^(Здравствуйте)|^(Доброе утро)|^(Добрый день)|^(Добрый вечер)'
# print(bool(search(regex, text, flags=IGNORECASE)))

#########################
# Напишите программу, которая определяет, в скольких публикациях содержится строка beegeek.
# from re import search, IGNORECASE
# from sys import stdin
#
# regex = r'beegeek'
# total = 0
# for line in stdin:
#     line = line.strip()
#     if search(regex, line, flags=IGNORECASE):
#         total += 1
#
# print(total)

#########################
# Вам доступна переменная article, содержащая некоторый многострочный текст. Дополните приведенный ниже код, чтобы он определил:
#
# количество строк, которые начинаются со слова Stepik (в произвольном регистре);
# количество строк, которые оканчиваются тремя точками ... или восклицательным знаком !.
# и вывел два соответствующих числа, каждое на отдельной строке.

# article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!
#
# Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
# В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...
#
# На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
# Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью.
#
# Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.
# Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!
#
# Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...
#
# Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''

# from re import findall, IGNORECASE, MULTILINE
# regex_s = r'^stepik'
# regex_ = r'\.{3}$|!$'
# print(len(findall(regex_s, article, IGNORECASE | MULTILINE)))
# print(len(findall(regex_, article, IGNORECASE| MULTILINE)))

#########################
# Напишите программу, которая принимает на вход строку текста и некоторое слово и определяет,
# сколько раз данное слово встречается как подслово в введенном тексте.

# from re import findall
# text = input()
# regex = input()
# print(len(findall( fr'\B{regex}\B', text)))


#########################
# Напишите программу, которая принимает на вход строку текста и некоторое слово и определяет,
# сколько вхождений данного слова содержится в введенном тексте.
# from re import findall
# text = input()
# regex = input()
# print(len(findall( fr'\b{regex}\b', text)))


#########################
# Американский английский и Британский английский языки имеют несколько различий, одно из которых наблюдается в написании слов.
# Например, слова, написанные на Американском английском языке и имеющие суффикс ze, в Британском варианте языка
# часто записываются с использованием суффикса se.
#
# Напишите программу, которая определяет, сколько раз слово встречается в тексте, учитывая его Британско-Американское написание.


# from re import findall, IGNORECASE
# regex = input()[:-2]
# text = input()
#
# print(len(findall( fr'\b{regex}(se|ze)\b', text, IGNORECASE)))

#########################
# Реализуйте функцию abbreviate(), которая принимает один аргумент:
#
# phrase — фраза
# Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.

# from re import findall
# def abbreviate(phrase):
#     return ''.join(findall(r'[A-Z]|\b[a-z]', phrase)).upper()
#
# print(abbreviate('javaScript object notation'))


#########################
# from re import sub, IGNORECASE
# def normalize_jpeg(filename):
#     return sub(r'(\.jpeg\b)|(\.jpg\b)', '.jpg', filename, flags=IGNORECASE)
#
# print(normalize_jpeg('stepik.jpeg.jpeg'))


# from re import finditer
# patern = r'(7-\d{3}-\d{3}-\d{2}-\d{2})|(8-\d{3}-\d{4}-\d{4})'
# for i in finditer(patern, input()):
#     print(i.group())


#########################
# Напишите программу, которая находит во фрагменте HTML-страницы все гиперссылки и выводит их составляющие — адресные части и указатели.
# from re import findall
# from sys import stdin
#
# regex = r'(?<=href=\").+?(?=</a>)'
# for line in stdin:
#     if 'href=' not in line:
#         continue
#     print(findall(regex, line)[0].replace('">', ', '))


#########################
# from re import findall
# from sys import stdin
#
# regex = r'(?<=href=\").+?(?=</a>)'
# for line in stdin:
#     if 'href=' not in line:
#         continue
#     print(findall(regex, line)[0].replace('">', ', '))


# import sys
# import re
#
# text = sys.stdin.read()
# pattern = r'<a href="(.+)">(.+)</a>'
#
# for address, pointer in re.findall(pattern, text):
#     print(f'{address}, {pointer}')


#########################


#
# import sys
# from bs4 import BeautifulSoup
# from collections import defaultdict
# result = defaultdict(set)
# for line in sys.stdin:
#     for tag in BeautifulSoup(line, "html.parser")():
#         result[tag.name] |= set(tag.attrs)
# for k, v in sorted(result.items()):
#     print(f"{k}: {', '.join(sorted(v))}")


#########################

# Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:
#
# filename — название файла, имеющее расширение jpeg или jpg, которое может быть записано
# буквами произвольного регистра
# Функция должна возвращать новое название файла с нормализованным расширением — jpg.
#
# import re
# def normalize_jpeg(name):
#     pattern = r'(.jpeg$)|(.jpg$)'
#     return re.sub(pattern, '.jpg', name, flags=re.IGNORECASE)
#
# print(normalize_jpeg('stepik.jpeg.jpeg'))
#########################

# Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна заменять все множественные пробелы в строке string на единственный
# пробел и возвращать полученный результат.

# import re
# def normalize_whitespace(string):
#     return re.sub(r'\s+', ' ', string)


# В Python существуют ключевые слова, которые нельзя использовать для
# названия переменных, функций и классов. Для получения списка всех ключевых
# слов можно воспользоваться атрибутом kwlist из модуля keyword.
# Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

# import keyword
# import re
#
# text = input()
# text = re.sub('\\b|\\b'.join(keyword.kwlist), r'<kw>', text, flags=re.IGNORECASE)
# print(text)


# Напишите программу, которая меняет местами первые две буквы в каждом слове, состоящем из двух или более букв.

# import re
# text = input()
# res = re.sub(r'\b(\w)(\w)(\w*)', r'\2\1\3',text)
#
# print(res)


# Напишите программу, которая раскрывает все умножения в тексте и выводит полученный результат.

# import re
#
# def func(match_obj):
#     s = match_obj.group(0)
#     num, sting = s.split('(')
#     return int(num) * sting.strip(')')
#
# text = input()
# while '(' in text:
#     text = re.sub(r'\d+\(\w+\)', func,text)
#
# print(text)


# Напишите программу, которая заменяет все повторяющиеся рядом стоящие слова на одно слово.


# import re
#
# text = re.sub(r'\b(\w+)(\W+?\1\b)+', r'\1', input())
#
# print(text)



# Напишите программу, которая разбивает строку по символам точки, запятой и точки с запятой.
# import re
#
# result = re.split(r'\s*[,;.]\s*', input())
#
# print(*result)



# Дано логическое выражение, состоящее из переменных, а также
# операторов |, &, and или or. Напишите программу, которая разбивает данную строку по указанным операторам.

# import re
#
# result = re.split(r'\s*[|&]\s*|(?:\s*and\s*)|(?:\s*or\s*)', input())
#
# print(*result, sep=', ')



# Реализуйте функцию multiple_split(), которая принимает два аргумента:
#
# string — строка
# delimiters — список строк
# Функция должна разбивать строку string на подстроки,
# используя в качестве разделителей строки из списка delimiters, и возвращать полученный результат в виде списка.

# import re
# def multiple_split(string, delimiters):
#     pattern = '|'.join([f'(?:{re.escape(i)})' for i in delimiters])
#     result = re.split(pattern, string)
#     return result




# Напишите программу, которая складывает все натуральные числа в строке, находящиеся в указанном диапазоне индексов.

# import re
# x, y = map(int, input().split())
# text = input()
#
# regex_obj = re.compile(r'\d+')
# result = regex_obj.findall(text, pos=x, endpos=y)
# print(sum(map(int,result)))


# Напишите программу, которая удаляет все комментарии из Python кода.
import sys
import re

text = sys.stdin.read()
text = re.sub(r'^\s*#.+\n', '', text, flags=re.MULTILINE)
text = re.sub(r'#.+', '', text)
text = re.sub(r' *\"{3}.+?\"{3}\n', '', text, flags=re.DOTALL)
print(text)

