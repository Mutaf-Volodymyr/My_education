# 1. Напишите функцию, которая принимает список кортежей от пользователя, где каждый
# кортеж содержит информацию о студенте (имя, возраст, средний балл).
# Программа должна вывести на экран имена студентов, чей средний балл выше заданного значения. Используйте методы кортежей и циклы для обработки данных.Выведите итоговый список на экран с помощью команды print.
    # Пример списка кортежей:
    # [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
    # Пример вывода:
# Введите пороговое значение среднего балла: 90
# Студенты с средним баллом выше 90 : ['Charlie']

#
# def my_function(my_list='[("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]', a=90):
#     my_list = my_list.strip('[]').split('),')  # [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
#     res = []
#     for i in my_list:
#         i = i.strip('() ')
#         i = i.split(', ')
#         i[0] = i[0].strip('\'"')
#         i[1] = int(i[1])
#         i[2] = int(i[2])
#         res.append(tuple(i))
#     result = []
#     for i in res:
#         if i[2] > a:
#             result.append(i[0])
#     return result
#
#
# print(my_function())
# print(my_function(my_list=input(), a=int(input())))



# 2. Напишите программу, которая принимает строку от пользователя и разбивает
# ее на отдельные слова. Затем программа должна создать новый кортеж, содержащий
# длину каждого слова в исходной строке. Используйте методы строк и кортежей для обработки данных.
    # Пример вывода:
    # Введите предложение: Программирование это интересно и полезно
    # Длины слов в предложении: (15, 3, 8, 2, 6)

# def my_function_2(a:str):
#     a = a.split()
#     res = []
#     for i in a:
#         res.append(len(i))
#     return tuple(res)
#
# print(my_function_2(a=input()))






