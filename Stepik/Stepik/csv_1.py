# Для построчного разделения текста удобно использовать строковый метод splitlines(), вместо метода split('\n').
# with open('products.csv', encoding='utf-8') as file:
#     data = file.read()
#     table = [r.split(',') for r in data.splitlines()]
from pprint import pprint


# ----------------------------Модуль csv
# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.reader(file)                               # создаем reader объект
#     for row in rows:
#         print(row)
#

# При создании reader объекта мы можем его настраивать, указывая:
# аргумент delimiter — односимвольная строка, используемая для разделения полей, по умолчанию имеет значение ','
# аргумент quotechar — односимвольная строка, используемая для кавычек в полях, содержащих специальные символы, по умолчанию имеет значение '"'.

# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=';', quotechar='"')
#     for index, row in enumerate(rows):
#         if index > 5:
#             break
#         print(row)

# ------------------------------------ DictReader
# В модуле csv есть специальный объект DictReader, который поддерживает создание объекта-словаря на основе названий столбцов.
# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     for row in rows:
#         print(row)

# -------------------------------------Запись данных с помощью writer
# import csv
#
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]
#
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(columns)
#     for row in data:
#         writer.writerow(row)

# newline функции open(), отвечает за переводы строк при чтении или записи
# в текстовый файл. По умолчанию имеет значение None, в этом случае все разделители строк преобразуются в '\n'

# Значение аргумента quoting=csv.QUOTE_NONNUMERIC означает, что в кавычки будут браться все нечисловые значения.
# По умолчанию символом кавычки является ", если нужно поменять символ, то используйте уже знакомый нам именованный аргумент quotechar.
#
# Для задания параметра quoting используются специальные константы из модуля csv:
# QUOTE_ALL: указывает объектам записи указывать все поля
# QUOTE_MINIMAL: указывает объектам записи заключать в кавычки только те поля, которые содержат специальные символы, такие
# ---------------как разделитель delimiter, кавычка quotechar или любой из символов в lineterminator
# QUOTE_NONNUMERIC: указывает объектам записи указывать все нечисловые поля
# QUOTE_NONE: указывает объектам записи никогда не заключать в кавычки поля



# ----------------Помимо метода writerow() можно использовать и метод writerows(),
# # ----------------чтобы записать сразу несколько строк. Единственным аргументом этого метода может быть коллекция коллекций.
# import csv
#
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]
#
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(columns)
#     writer.writerows(data)


# ------------------------DictWriter
# Для записи данных в csv файл также можно использовать DictWriter объект, который позволяет записывать содержимое словаря в файл.
# import csv
#
# data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
#         {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
#         {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]
#
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
#
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()                 # запись заголовков
#     for row in data:                     # запись строк
#         writer.writerow(row)





# ________________________________ ЗАДАЧИ

# import csv
# with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
#     # создаем writer объект и указываем названия столбцов
#     writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
#     # записываем первую строку с названиями столбцов
#     writer.writeheader()
#     # записываем строку с данными
#     writer.writerow({'first_col': 'value1', 'second_col': 'value2'})

# _______________________

# Наступил ноябрь, и во многих магазинах начались распродажи, но как многим известно, зачастую товары
# со скидкой оказываются дороже, чем без нее. Вам доступен файл sales.csv, который содержит данные о
# ценообразовании различной бытовой техники. В первом столбце записано название товара, во втором — старая цена,
# в третьем — новая цена со скидкой:
# ---name;old_price;new_price
# ---Встраиваемая посудомоечная машина De'Longhi DDW 06S;23089;31862
# ---Вытяжка Falmec Afrodite 60/600;27694;18001
# Напишите программу, которая выводит названия тех товаров, цена на которые уменьшилась. Товары должны
# быть расположены в своем исходном порядке, каждый на отдельной строке.

# import csv
# with open('csv_1/sales.csv', 'r', encoding='utf-8') as sales:
#     file = csv.DictReader(sales, delimiter=';')
#     file = filter(lambda row: int(row['old_price']) > int(row['new_price']), file)
#     for row in file:
#         print(row['name'])


# -----------------------------------------
# Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных компаниях.
# В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:
#
# company_name;salary
# Atos;135000
#
# Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их названия,
# каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, они должны быть расположены в
# лексикографическом порядке их названий.
# Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат к их количеству.
# Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом кавычки не используются.

#
# import csv
# with open('csv_1/salary_data.csv', 'r', encoding='utf-8') as salary:
#     file = list(csv.reader(salary, delimiter=';'))
#     del file[0]
#     res = dict()
#     for name, sal in file:
#         if name not in res:
#             res[name] = [int(sal)]
#         else:
#             res[name].append(int(sal))
#     print(*sorted(res, key=lambda x: sum(res[x]) / len(res[x])), sep='\n')

# более успешная реализация через метот get
# for key, value in rows[1:]:
#     name[key] = name.get(key, []) + [int(sal)]



# -------------------------------------------------
# Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа, либо строковые значения:
#
# Machete,2010,72
# Marvin's Room,1996,80
# Raging Bull,1980,97
# ...
# Напишите программу, которая сортирует содержимое данного файла по указанному столбцу. Причем данные должны быть
# отсортированы в порядке возрастания чисел, если столбец содержит числа, и в лексикографическом порядке слов,
# если столбец содержит слова.

# import csv
# n = int(input())
# with open('csv_1/deniro.csv', 'r', encoding='utf-8') as deniro:
#     file = [[i[0], int(i[1]), int(i[2])] for i in  csv.reader(deniro)]
#     for i in sorted(file, key=lambda x: x[n-1]):
#         print(*i, sep=',')


# ---------------------------------------
# Реализуйте функцию csv_columns(), которая принимает один аргумент:
# filename — название csv файла, например, data.csv
# Функция должна возвращать словарь, в котором ключом является название столбца файла filename,
# а значением — список элементов этого столбца.

# def csv_columns(filename) -> dict:
#     import csv
#     with open(filename, 'r', encoding='utf-8') as file:
#         rows = list(csv.reader(file))
#         result = {}
#         for value in rows[1:]:
#             for i in range(len(rows[0])):
#                result[rows[0][i]] = result.get(rows[0][i], []) + [value[i]]
#         return result


# функция здорового человека
# def csv_columns(filename):
#     with open(filename, encoding="utf-8") as file_in:
#         rows = list(csv.reader(file_in))
#         return {key: value for key, *value in zip(*rows)}

# https://github.com/python-generation/Professional/blob/main/Module_4/Module_4.2/Module_4.2.15/input.txt

# -------------------------------------------------------
# Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
# В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:
#
# first_name,surname,email
# John,Wilson,johnwilson@outlook.com
# Mary,Wilson,marywilson@list.ru
# ...
# Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:
#
# domain,count
# rambler.ru,24
# iCloud.com,29
# ...
# где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный домен.
# Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении количества
# использований — в лексикографическом порядке.

# import csv
# with open('csv_1/data.csv', 'r', encoding='utf-8') as data, open('csv_1/domain_usage.csv', 'w', newline='') as outfile:
#     file = csv.reader(data)
#     next(file)
#     res = {}
#     for first_name, surname, email in file:
#         email = email[email.index('@')+1:]
#         res[email] = res.get(email, 0) + 1
#     writer = csv.writer(outfile, delimiter=',')
#     writer.writerow(['domain','count'])
#     for row in sorted(res.items(), key=lambda x: (x[1], x[0])):
#         writer.writerow(row)

# --------------------------------
# Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы. В первом столбце записано название
# округа, во втором — название района, в третьем — адрес, в четвертом — количество точек доступа по этому адресу:
#
# adm_area;district;location;number_of_access_points
# Центральный административный округ;район Якиманка;город Москва, улица Серафимовича, дом 5/16;5
# Центральный административный округ;район Якиманка;город Москва, Болотная набережная, дом 11, строение 1;2
# ...
# Напишите программу, которая определяет количество точек доступа в каждом районе Москвы и выводит названия всех районов,
# для каждого указывая соответствующее количество точек доступа, каждое на отдельной строке, в следующем формате:
# # <название района>: <количество точек доступа>

# Названия районов должны быть расположены в порядке убывания количества точек доступа, при совпадении количества точек
# доступа — в лексикографическом порядке.

# import csv
# with open('csv_1/wifi.csv', 'r', encoding='utf-8') as wifi:
#     file = csv.reader(wifi, delimiter=';')
#     next(file)
#     res = {}
#     for row in file:
#         res[row[1]+':'] = res.get(row[1]+':', 0) + int(row[3])
#
# for row in sorted(res.items(), key=lambda x: (-x[1],x[0])):
#     print(*row)

# --------------------------------
# Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник.
# В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано
# полное имя пассажира, в третьем — пол, в четвертом — возраст:
#
# survived;name;sex;age
# 0;Mr. Owen Harris Braund;male;22
# 1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
# ...
# Напишите программу, которая выводит имена выживших пассажиров, которым было менее
# 18 лет, каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола,
# а затем — женского, имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

# import csv
# with open('csv_1/titanic.csv', 'r', encoding='utf-8') as titanic:
#     file = sorted(list(csv.reader(titanic, delimiter=';'))[1:], key=lambda x: x[2], reverse=True)
#     file = [i[1]  for i in file if i[0] == '1' and float(i[3]) < 18]
#     print(*file, sep='\n')


# -------------------------------------------
# Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
# В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты,
# в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:
#
# username,email,dtime
# rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
# busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
# ...
# Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для
# каждого пользователя и записывает их в файл new_name_log.csv. В файле new_name_log.csv первой
# строкой должны быть заголовки столбцов такие же, как в файле name_log.csv. Логи в итоговом
# файле должны быть расположены в лексикографическом порядке названий электронных ящиков пользователей.

# import csv
# from datetime import datetime
#
# with open('csv_1/name_log.csv', 'r', encoding='utf-8') as name_log, open('csv_1/new_name_log.csv', 'w', newline='') as outfile:
#     patern = '%d/%m/%Y %H:%M'
#     file =  csv.reader(name_log)
#     title = next(file)
#     file = sorted([[username, email, datetime.strptime(dtime, patern)] for username, email, dtime  in file], key= lambda x: x[2])
#     res = {i[1]: [i[0], i[1], i[2].strftime(patern)] for i in file}
#     writer = csv.writer(outfile, delimiter=',')
#     writer.writerow(title)
#     for row in sorted(res.values(), key=lambda x: x[1]):
#         writer.writerow(row)

# -----------------------------------------
# Рассмотрим следующий текстовый фрагмент:
# ball,color,purple
# ball,size,4
# ball,notes,it's round
# cup,color,blue
# cup,size,1
# cup,notes,none

# Каждая строка этого фрагмента содержит три значения через запятую: имя объекта,
# свойство этого объекта, значение свойства. Например, в первой строке указан объект ball,
# имеющий свойство color, значение которого равно purple. Также у объекта ball есть свойства
# size и notes, имеющие значения 4 и it's round соответственно. Помимо объекта ball имеется
# объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам общее
# название object и сгруппируем строки данного текстового фрагмента по первому столбцу:
# object,color,size,notes
# ball,purple,4,it's round
# cup,blue,1,none
# Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта,
# а в последующих — значения соответствующих свойств этого объекта.
# Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:
# filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату текстового фрагмента, рассмотренного в условии задачи: каждая строка файла содержит три значения через запятую, а именно имя объекта, свойство этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
# id_name — общее название для объектов
# Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.

# def condense_csv(filename, id_name):
#     import csv
#     with open(filename, 'r', encoding='utf-8') as file, open('condensed.csv', 'w', encoding='utf-8', newline='') as outfile:
#         rows = list(csv.reader(file))
#         a = len({i[1] for i in rows})
#         res = [id_name]
#         res.extend([rows[i][1] for i in range(a)])
#         res = [res]
#         for i in range(0, len(rows), a):
#             b = [rows[i][0]]
#
#             for j in range(a):
#                 b.append(rows[i+j][-1])
#             res.append(b)
#         writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_NONE)
#         writer.writerows(res)

# -----------------------------------------
# вам доступен файл student_counts.csv, который содержит данные о количестве учеников в некотором учебном заведении за период
# 2000 - 2021 г. В первом столбце записан год, в последующих столбцах записан класс и количество учеников в данном классе в этом году:
#
# year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
# 2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
# 2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
# ...
# Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv,
# располагая все столбцы в порядке возрастания классов, при совпадении классов — в порядке возрастания букв.

# решение курильщика (мое)
# import csv
# def class_sort(class_dict):
#     sort_dict = dict()
#     sort_dict['year'] = class_dict.pop('year')
#     class_dict = sorted(list(class_dict.items()), key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1]))
#     for key, value in class_dict:
#         sort_dict[key] = value
#     return sort_dict
#
# with open('csv_1/student_counts.csv', 'r', encoding='utf-8') as student, open('csv_1/sorted_student_counts.csv', 'w', encoding='utf-8') as outfile:
#     file = list(csv.DictReader(student))
#     result = []
#     for row in file:
#         result.append(class_sort(row))
#     writer = csv.DictWriter(outfile, fieldnames = result[0].keys(), delimiter=',', quoting=csv.QUOTE_NONE)
#     writer.writeheader()
#     writer.writerows(result)

# решение здорового человека
# import csv
#
# def key_func(grade):
#     number, letter = grade.split('-')
#     return int(number), letter
#
# with open('student_counts.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
#     rows = list(reader)
#
# with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(rows)

# -----------------------------------------
# Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт, а также магазин,
# в котором он продается. Вам доступен файл prices.csv, который содержит информацию о ценах продуктов в различных магазинах.
# В первом столбце записано название магазина, а в последующих — цена на соответствующий товар в этом магазине:
#
# Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;Вареники;Картофель;Батончик
# Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
# Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
# ...
# Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина, в котором он продается, в следующем формате:
# <название продукта>: <название магазина>
# Если имеется несколько самых дешевых товаров, то следует вывести тот товар, чье название меньше в лексикографическом сравнении. Если один
# товар продается в нескольких магазинах по одной минимальной цене, то следует вывести тот магазин, чье название меньше в лексикографическом сравнении.

# import csv
# import time
# start_time1 = time.time()
# with open('csv_1/prices.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     market, product, price = '', 'я'*10, 10**10
#     for row in reader:
#         for key, val in row.items():
#             if val.isdigit() and int(val) <= price and key < product:
#                 price = int(val)
#                 market = row['Магазин']
#                 product = key
#
#     print(product, market, sep=': ')
# print(time.time() - start_time1)
#
# # решение лаконичней и немного быстрее, но есть предположение, что оперативки кушает больше
# import csv
# import time
# start_time2 = time.time()
# with open('csv_1/prices.csv', encoding='UTF-8') as f:
#     h, *rows = csv.reader(f, delimiter=';')
# goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
# cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))
#
# print(f'{cheapest[1]}: {cheapest[0]}')
# print(time.time() - start_time2)


