########## OS ###############
# Данный модуль обеспечивает портативный способ использования
# функциональных возможностей, зависящих от операционной системы.

# имя текущей ОС
# import os
# print(os.name)

# сведения, которые касаются конфигурации компьютера
# import os
# print(os.environ)


# получить доступ к различным переменным среды
# import os
# print(os.getenv("PATH"))

#  Получить сведения о текущей директории
# import os
# print(os.getcwd())
# При желании, рабочую директорию можно настроить по своему усмотрению,
# применив метод chdir из библиотеки os. Для этого необходимо передать ему
# в качестве параметра абсолютный адрес к новому каталогу.


# Сообщает о наличии/отсутствии указанного объекта в памяти компьютер
# import os
# print(os.path.exists("/Users/vladimirmutaf/Documents/IT/My_education/Stepik/Stepik/os_shutil_shelve.py"))

# Проверить, является ли определенный объект файлом, поможет функция isfile.
# import os
# print(os.path.isfile("/Users/vladimirmutaf/Documents/IT/My_education/Stepik/Stepik/os_shutil_shelve.py"))

# проверка объекта на принадлежность к классу директорий
# import os
# print(os.path.isdir("/Users/vladimirmutaf/Documents/IT/My_education/Stepik/Stepik"))

# создать папку
# import os
# os.mkdir(r"/Users/vladimirmutaf/Documents/IT/My_education/Stepik/Stepik/test")

# создать папку рекурсивно
# import os
# os.makedirs(r"/Users/vladimirmutaf/Documents/IT/My_education/Stepik/Stepik/test1/test2")

# удалит файл
# import os
# os.remove(r"путь")

# удалит файл директорию
# import os
# os.rmdir(r"путь")

# удалит файл директорию рекурсивно с родительскими если они пустые
# import os
# os.removedirs(r"путь/путь/путь")


# запускать отдельные файлы и папки прямиком из программы ??????????? не работает
# import os
# os.startfile(r"/Users/vladimirmutaf/Documents/IT/My_education/Stepik/Stepik/Zip_1/Zip_metod.png")

# Преобразовать адрес объекта в название позволяет функция basename
# import os
# print(os.path.basename("/Users/vladimirmutaf/Documents/IT/My_education/Stepik/Stepik/Zip_1/Zip_metod.png"))

# переименование
# import os
# os.rename(r"D:\folder", r"D:\catalog")


# Содержимое директорий
# import os
# print(os.listdir(r"D:\folder"))

######################### shutil ######################
# Данный  модуль сохраняет объекты в файл с определенным ключом.
# Затем по этому ключу можно извлечь ранее сохраненный объект из файла.
# import shutil



######################### shelve ######################
# Данный  модуль сохраняет объекты в файл с определенным ключом.
# Затем по этому ключу можно извлечь ранее сохраненный объект из файла.

import shelve

