####################### ZipFile ######################
import os
import zipfile
# from zipfile import ZipFile
# with ZipFile('test.zip', mode = 'r') as zip_file:
#     zip_file.printdir()
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)


# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read().decode('utf-8'))

# При создании объекта ZipFile мы также можем передать еще два необязательных аргумента:
    # compression, который определяет метод сжатия, который должен использоваться при записи в архив.
                # Он принимает одно из значений: ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA.
                # По умолчанию используется значение compression=ZIP_STORED
    # allowZip64, который позволяет разрешить использование расширений zip64,
    # которые дают возможность создавать архивы размером больше 4 гигабайт. По умолчанию равен allowZip64=True
# Для того чтобы проверить является ли некоторый файл zip архивом, используется функция zipfile.is_zipfile(),
# которая принимает на вход путь к файлу (или сам файловый объект) и возвращает значение True,
# если указанный файл является zip архивом, или False в противном случае.


# from zipfile import ZipFile
# with ZipFile('Zip_1/workbook.zip', 'r') as zip_file:
#     info = zip_file.infolist()
#     print(info)


# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное число — количество файлов в этом архиве.

# from zipfile import ZipFile
# with ZipFile('Zip_1/workbook.zip', 'r') as zip_file:
#     info = zip_file.infolist()
#     total = 0
#     for name in info:
#         if not name.is_dir():
#             total += 1
#     print(total)



# ам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу,
# которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах

# from zipfile import ZipFile
# with ZipFile('Zip_1/workbook.zip', 'r') as zip_file:
#     total = 0
#     total_compress = 0
#     info = zip_file.infolist()
#     for i in info:
#         total += i.file_size
#         total_compress += i.compress_size

# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.

# from zipfile import ZipFile
# with ZipFile('Zip_1/workbook.zip', 'r') as zip_file:
#     di = {}
#     info = zip_file.infolist()
#     for i in info:
#         if i.file_size != 0:
#             di[i.filename] = i.compress_size / i.file_size
#     print(min(di, key=di.get).split("/")[-1])


# апишите программу, которая выводит названия файлов из этого архива, которые были созданы или изменены позднее
# 2021-11-30 14:22:00. Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.

# from zipfile import ZipFile
# from datetime import datetime
# from os import path
# with ZipFile('Zip_1/workbook.zip', 'r') as zip_file:
#     date_1 = datetime(year=2021, month=11, day=30, hour=14, minute=22, second=0)
#     info = filter(lambda x: datetime(*x.date_time) > date_1, zip_file.infolist())
#     info1 = map(lambda x: path.basename(x.filename), info)
#     print(*sorted(filter(None, info1)), sep='\n')


# Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке,
# указывая для каждого его дату изменения, а также объем до и после сжатия

# from zipfile import ZipFile
# from datetime import datetime
# from os import path
# with ZipFile('Zip_1/workbook.zip', 'r') as zip_file:
#     res = {path.basename(el.filename): [el.date_time, el.file_size, el.compress_size] for el in zip_file.infolist() if not el.filename.endswith('/')}
#     for key, value in sorted(res.items()):
#         print(key)
#         print(f'  Дата модификации файла: {datetime(*value[0])}\n'
#               f'  Объем исходного файла: {value[1]} байт(а)\n'
#               f'  Объем сжатого файла: {value[2]} байт(а)\n')


# Вам доступен набор различных файлов, названия которых представлены в списке file_names.
# Дополните приведенный ниже код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка.

# from zipfile import ZipFile
#
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#
# with ZipFile('files.zip', mode='w') as zip_file:
#     for f in file_names:
#         zip_file.write(f)




# Вам доступен набор различных файлов, названия которых представлены в списке file_names. Также вам доступен архив files.zip.
# Дополните приведенный ниже код, чтобы он добавил в архив files.zip только те файлы из списка file_names, объем которых не превышает 100 байт.

# from zipfile import ZipFile
# import os.path
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#
# with ZipFile('files.zip', mode='a') as zip_file:
#     for f in file_names:
#         if os.path.getsize(f) <= 100:
#             zip_file.write(f)


# Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:
#
# zip_name — название zip архива, например, data.zip
# *args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
# Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни одного названия файла для извлечения,
# то функция должна извлечь все файлы из архива.

# from zipfile import ZipFile
# def extract_this(zip_name, *args):
#     with ZipFile(zip_name) as zip_file:
#         if args:
#             for arg in args:
#                 zip_file.extract(arg)
#         else:
#             zip_file.extractall()




# Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов,
# каждый из которых содержит информацию о каком-либо футболисте:
# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
# выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а
# при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.

# from zipfile import ZipFile
# import json
#
# with ZipFile('Zip_1/data.zip') as zip_file:
#     res = []
#     for i in zip_file.namelist():
#
#         if i.endswith('.json'):
#             try:
#                 with zip_file.open(i) as file:
#                     res.append(json.loads(file.read().decode('utf-8')))
#             except:
#                 pass
#     res1 = filter(lambda x: x['team'] == 'Arsenal', res)
#     res2 = map(lambda x: x['first_name'] + ' ' + x['last_name'] , res1)
#     print(*sorted(res2), sep='\n')


# Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу,
# которая выводит его файловую структуру и объем каждого файла.

# def convert_bytes(size):
#     """Конвертер байт в большие единицы"""
#     if size < 1000:
#         return f'{size} B'
#     elif 1000 <= size < 1000000:
#         return f'{round(size / 1024)} KB'
#     elif 1000000 <= size < 1000000000:
#         return f'{round(size / 1048576)} MB'
#     else:
#         return f'{round(size / 1073741824)} GB'
#
# from zipfile import ZipFile
# with ZipFile('Zip_1/desktop.zip') as zip_file:
#     info = zip_file.infolist()
# for row in info:
#     res = row.filename.split('/')
#     # print(res)
#     if res[-1] == '':
#         print('  ' * (len(res) - 2), res[-2], sep='')
#     else:
#         print('  ' * (len(res) - 1), res[-1], ' ', convert_bytes(row.file_size), sep='')






