# num1 = 100
# num2 = 100
#
# num3 = 10**33
# num4 = 10**33
#
# print(num1 is num2, num1 == num2)
# print(num3 is num4, num3 == num4)

# -------------------------

# s1 = 'b' * 4096
# s2 = 'b' * 4096
#
# s3 = 'b' * 5000
# s4 = 'b' * 5000
#
# print(s1 is s2)
# print(s3 is s4)

# --------------------------
# import sys
# s1 = sys.intern('b' * 5000)
# s2 = sys.intern('b' * 5000)
# s3 = 'b' * 5000
# s4 = 'b' * 5000
# print(s1 is s2)
# print(s3 is s4)
# print(s2 is s3)


# --------------------------
# age = 18
# data = {'Arthur': age, 'Dima': age, 'Timur': age}
# age = 29
#
# print(data['Timur'])

# --------------------------
# nums1 = [1, 2, [3], 4]
# nums2 = nums1[2]
# nums2.append(10)
#
# print(nums1)

# --------------------------
# def add_ten(data):
#     data.append(10)
#     return data
#
# nums = [1, 2, 3]
# print(nums, add_ten(nums), nums)



# --------------------------
# def change_list(data):
#     data = [10]
#     return data
#
# nums = [1, 2, 3]
# change_list(nums)
#
# print(nums)

# --------------------------
# nums1 = [1, 2]
# nums2 = nums1
# nums2 = nums2 + [3, 4]
#
# print(nums1)
# print(nums2)
#
# print('-'*20)
#
# nums3 = [1, 2]
# nums4 = nums3
# nums4 += [3, 4]
#
# print(nums3)
# print(nums4)



# --------------------------
# def add_ten():
#     data=[]
#     data.append(10)
#     return data
# print(add_ten())
# print(add_ten())
# print(add_ten())

# def add_ten(data=[]):
#     data.append(10)
#     return data
# print(add_ten())
# print(add_ten())
# print(add_ten())


# --------------------------
# def add_ten(data=None):
#     if data is None:
#         data = []
#     data.append(10)
#     return data
#
# print(add_ten())
# print(add_ten())
# print(add_ten())

#  Поверхностное копирование создает отдельный новый объект,
#  но вместо копирования дочерних элементов в новый объект,
#  оно просто копирует ссылки на их адреса памяти

# import copy
#
# data1 = [1, 2, 3]
# data2 = copy.copy(data1)
# data1.append(4)
#
# print(id(data1), data1)
# print(id(data2), data2)
#
# print(id(data1[0]), data1)
# print(id(data2[0]), data2)

# --------------------------

# import copy
#
# data1 = [[1, 2, 3], [4, 5, 6]]
# data2 = copy.copy(data1)
#
# data1[0].append(7)
# data2[1].append(8)
#
# print(id(data1), data1)
# print(id(data2), data2)


# Глубокое копирование создает новую и отдельную копию всего объекта
# со своим уникальным адресом памяти. Это означает, что любые изменения,
# внесенные вами в новую копию объекта, не будут отражаться в исходной, и наоборот.

# import copy
#
# data1 = [[1, 2, 3], [4, 5, 6]]
# data2 = copy.deepcopy(data1)
#
# data1[0].append(7)
# data2[1].append(8)
#
# print(id(data1), data1)
# print(id(data2), data2)


# Встроенные функции, используемые при создании коллекций (list, set, dict, ...),
# также могут быть использованы для создания поверхностной копии объектов.


# data1 = [1, 2, 3, 4]
# data2 = {'a': 1, 'b': 2}
# data3 = {1, 2, 3, 4}
#
# new_data1 = list(data1)
# new_data2 = dict(data2)
# new_data3 = set(data3)
#
# print(data1 is new_data1, data1 == new_data1)
# print(data2 is new_data2, data2 == new_data2)
# print(data3 is new_data3, data3 == new_data3)

# Поверхностную копию списка также можно создать с помощью среза всего списка.

# Для определения размера объектов встроенных типов можно использовать функцию getsizeof()
# модуля sys. Данная функция возвращает размер объекта в байтах.
# import sys
#
# print(sys.getsizeof(10))
# print(sys.getsizeof(True))
# print(sys.getsizeof(None))
# print(sys.getsizeof(''))
# print(sys.getsizeof('beegeek'))


# помощью функции getsizeof() нельзя вычислять размер сложных объектов,
# содержащих вложенные структуры (списки списков и т.д.).
# Для того чтобы правильно определять размер абсолютно любого объекта (включая пользовательские)
# в Python используется функция asizeof() модуля asizeof, который находится в библиотеке pympler.


# --------------------------
# Для получения количества ссылок на заданный объект используется функция
# getrefcount() из модуля sys.

# import sys
#
# nums = [1, 2, 3]
#
# print(sys.getrefcount(nums))

# --------------------------
# import sys
#
# nums = [1, 2, 3]                            # ссылка 1
# nums1 = nums                                # ссылка 2
# nums2 = nums1                               # ссылка 3
# temp = [4, 5, 6, nums, nums1, nums2]        # ссылка 4, 5, 6
# print(sys.getrefcount(nums))


# Алгоритм подсчета ссылок очень простой и эффективный, но у него есть один большой недостаток.
# Он не умеет определять циклические ссылки.
# Приведенный ниже код:
#
# nums1 = [1, 2, 3]
# nums2 = [4, 5]
#
# nums1.append(nums2)
# nums2.append(nums1)
# создает циклические ссылки, так как nums1 содержит ссылку на nums2, в то время как nums2
# содержит ссылку на nums1. Таким образом, счетчики ссылок у nums1 и nums2
# никогда не будут равны нулю.

# Для взаимодействия со сборщиком мусора используется модуль gc.
#
# Наиболее полезные функции модуля:
#
    # gc.enable(): включает сборщика мусора (по умолчанию он включен)
    # gc.disable(): отключает сборщика мусора
    # gc.isenabled(): возвращает True, если сборщик мусора включен, или False в противном случае
    # gc.collect(): запускает сборщика мусора на всех трех поколениях.
                    # Функция имеет необязательный аргумент generation (целое число от 0 до 2),
                    # указывающий номер поколения, в котором нужно запустить сборщика мусора


# https://habr.com/ru/companies/wunderfund/articles/328404/

