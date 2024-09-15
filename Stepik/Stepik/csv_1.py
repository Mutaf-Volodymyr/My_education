# Для построчного разделения текста удобно использовать строковый метод splitlines(), вместо метода split('\n').
# with open('products.csv', encoding='utf-8') as file:
#     data = file.read()
#     table = [r.split(',') for r in data.splitlines()]

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


















