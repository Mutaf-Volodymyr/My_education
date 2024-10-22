####################### ZipFile ######################


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



