
# Вам доступен список files, содержащий названия различных файлов. Дополните приведенный ниже код,
# чтобы он вывел все расширения файлов, присутствующие в списке files, указав для каждого количество
# файлов с данным расширением. Расширения должны быть расположены в лексикографическом порядке,
# каждый на отдельной строке, в следующем формате


# from collections import Counter
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
#
# res = Counter([i.split('.')[1] for i in files])
# for key, value in sorted(res.items()):
#     print(f'{key}: {value}')

###############################################################

# Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:
    # word — слово
    # words — последовательность слов, разделенных пробелом
# Функция должна определять, сколько раз слово word встречается в последовательности words, и возвращать полученный результат.

# from collections import Counter
# def count_occurences(word, words):
#     res = Counter(map(str.lower, words.split()))
#     return res[word.lower()]

###############################################################
# Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами,
# то вместо указания количества товара числом, он добавляет его в список столько раз, сколько планирует купить.
# Все товары Тимур записывает в нижнем регистре через запятую.
# Напишите программу, которая выводит все товары из данного списка покупок, указывая для каждого его количество.


# from collections import Counter
# res = Counter([i for i in input().split(',')])
# for key, value in sorted(res.items()):
#     print(f'{key}: {value}')


###############################################################

# Тимур живет в мире, в котором цена товара определяется как сумма Unicode кодов букв его названия. Буквенным обозначением данной валюты являются две заглавные латинские буквы UC. Например, ручка в его мире стоит:
#
# 1088+1091+1095+1082+1072=5428UC
# Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами, то вместо указания количества товара числом, он добавляет его в список столько раз, сколько планирует купить. Все товары Тимур записывает в нижнем регистре через запятую.
#
# Напишите программу, которая группирует одинаковые товары из данного списка покупок и определяет стоимость каждой группы.

# from collections import Counter
# res = Counter([i for i in input().split(',')])
# n = len(max(res.keys(), key=len))
# for key, value in sorted(res.items()):
#     summ = sum((ord(i) for i in key if i != ' '))
#     print(f'{key.ljust(n)}: {summ} UC x {value} = {summ * value} UC')



###############################################################
# Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:
# Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и их количество должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:
# <буква>: <количество>

# from collections import Counter
# with open('Counter_1/pythonzen.txt', 'r', encoding='utf-8') as file:
#     text = file.read().replace('\n', '')
#     res = Counter(i.lower() for i in text if i.isalpha())
# for key, value in sorted(res.items()):
#     print(f'{key}: {value}')


###############################################################
# Дана последовательность слов. Напишите программу,
# которая выводит наиболее часто встречаемое слово в этой последовательности.

# from collections import Counter
# res = Counter(input().lower().split())
# print(res.most_common(1)[0][0])


###############################################################
# Дана последовательность слов. Напишите программу, которая выводит наименее часто встречаемое слово
# в этой последовательности. Если таких слов несколько, программа должна вывести их все.

# from collections import Counter
# res = Counter(input().lower().split()).most_common()
# mn = res[-1][1]
# res = sorted((i[0] for i in filter(lambda x: x[1] == mn, res)))
# print(*res, sep=', ')



###############################################################
# Дана последовательность слов. Напишите программу, которая выводит наиболее часто
# встречаемое слово в этой последовательности. Если таких слов несколько,
# программа должна вывести то, которое больше в лексикографическом сравнении.


# from collections import Counter
# res = Counter(input().lower().split()).most_common()
# print(max(res, key=lambda x: (x[1], x[0]))[0])



###############################################################
# Дана последовательность слов. Напишите программу, которая группирует слова из этой последовательности
# по их длине и определяет количество слов в каждой полученной группе.

# from collections import Counter
# res = Counter(len(i) for i in input().lower().split())
# for k, v in sorted(res.items(), key=lambda x: (x[1])):
#     print(f'Слов длины {k}: {v}')



###############################################################
# Дан список имен учеников и их оценок за экзамен. Напишите программу,
# которая определяет второго по счету ученика, имеющего самую низкую оценку.

# import sys
# from collections import Counter
#
# data = Counter()
# for i in sys.stdin.read().split('\n'):
#     k, v = i.split()
#     data.update(Counter({k: int(v)}))
#
# print(data.most_common()[-2][0])


###############################################################

# Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
    # symbols — набор символов
    # word — слово
# Функция должна возвращать True, если из набора символов symbols можно составить слово word, или False в противном случае.
from collections import Counter
# def scrabble(symbols, word):
#     w = Counter(word.lower())
#     s = Counter(symbols.lower())
#     s.subtract(w)
#     return not bool(-s)
#
# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
# print(scrabble('begk', 'beegeek'))
# print(scrabble('beegeek', 'beegeek'))

# Реализуйте функцию print_bar_chart(), которая принимает два аргумента в следующем порядке:
    # data — строка или список строк
    # mark — одиночный символ
# Функция должна определять:
    # сколько раз встречается каждый символ в строке, если data является строкой
    # сколько раз встречается каждая строка в списке, если data является списком
# Затем функция должна выводить результат в виде столбчатой диаграммы, указывая каждый символ (строку)
# и его количество. Количество отображается как повторение символа mark соответствующее число раз,
# например, если mark='+', то количество, равное четырем, будет отображено как ++++. Символы (строки)
# в диаграмме должны быть расположены в порядке уменьшения количества, при равных количествах —
# в своем исходном порядке, каждая на отдельной строке, в следующем формате:

# from collections import Counter
# def print_bar_chart(data, mark):
#     res = Counter(data)
#     mx = len(max(res.keys(), key=len))
#     for k, v in sorted(res.items(), key=lambda x: x[1], reverse=True):
#         print(f'{k.ljust(mx)} |{mark*v}')


