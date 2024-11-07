# from string import punctuation
#
# with open('anna-karenina_u8.txt', 'r', encoding='utf-8') as f:
#         text = f.read().split()
#         text1 = filter(lambda y: len(y) > 10, map(lambda x: x.strip(punctuation+'«').lower(), text))
#         print(*text1, sep='\n')


# # 1
# from functools import reduce
# strings = ["apple", "banana", "cherry"]
# print(sum(map(len, strings)))
# print(reduce(lambda x, y: x + len(y), strings, 0))

# 2 Создать новый список, содержащий суммы соответствующих элементов
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# print(list(map(sum, zip(list1, list2))))

# 3 Конвертировать списка строк чтобы каждая строка начиналась с заглавной буквы,
# а остальные буквы были маленькие (стРОкА -> Строка)
# strings = ["стРОкА", "другаЯ стРОка", "последняя строкА"]
# print(*map(str.title, strings))




# numbers = [0, -1, 2, 3, -4, 5, -6, 7, 8, -9]
# # возвести каждое положительное число в квадрат, найти их сумму
# print(sum(map(lambda x:x**2, filter(lambda x:x>0, numbers))))


# import itertools
# import operator
# numbers = [1, 2, 3, 4, 5]
# result = itertools.accumulate(numbers, operator.mul)
# print(result)

#######################

res = map(lambda x: x**2, filter(lambda x: x % 2 ==0, map(lambda x: x**2, map(int, input().split()))))
print(*res)

res = map(lambda x: x**4, filter(lambda x: x % 2 ==0, map(int, input().split())))
print(*res)


# Сгенерировать все пароли, состоящие из 4 символов чтобы среди них была хотя бы одна большая латинская буква, одна маленькая, одна цифра и никаких иных типов символов.
# При этом запрещено, чтобы символ повторялся в пароле или две соседние по алфавиту буквы стояли рядом. Записать полученные пароли в файл.















