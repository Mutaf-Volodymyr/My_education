# # Практическое задание 1
# # Дан массив.
# # Дать ответ на вопрос есть ли в нём два элемента с суммой ноль.
# # ● Решить с двумя вложенными циклами
# # ● Решить с помощью множеств
#
# li = [-1, 0, 5, 0, 10, 1]
# li2 = [-1, 0, 5, 0, 10, -1]
# li3 = [-1, 0, 5, 10, -1]
# def lalala(a):
#     for i, el in enumerate(a):
#         for j, el2 in enumerate(a):
#             if el + el2 == 0 and i != j:
#                 return True
#     return False
#
# print(lalala(li))
# print(lalala(li2))
# print(lalala(li3))
#
#
#
# li = [-1, 0, 5, 0, 10, 1]
# li2 = [-1, 0, 5, 10, -1]
# li3 = [-1, 0, 5, 10, 1]
#
# def blablabla(a:list):
#     if a.count(0) > 1:
#         return True
#     a = set(a)
#     a_len = len(a)
#     b = {abs(i) for i in a}
#     return a_len != len(b)
#
#
# print(blablabla(li))
# print(blablabla(li2))
# print(blablabla(li3))


# 6. Напишите функцию, которая получает на вход три слова и определяет, являются ли они
# анаграммами друг друга. Использовать множества. Функция возвращает true, если слова
# являются анаграммами и false в противном случае. Пример: anagram(“кластер”, “стрелка”,
# “сталкер”) = true.

# def lalalend(*args):
#     if len(set(map(len, args))) != 1:
#         return False
#     res = {frozenset(i) for i in args}
#     print(res)
#     return len(res) == 1


# print(lalalend('кластер', 'стрелка', 'сталкер'))
# print(lalalend('кластер', 'стрелка', 'сталллкер'))
# print(lalalend('кластер', 'стрелкэ', 'стажкер'))



# 9. Напишите функцию, которая получает на вход две строки с перечислением интересов и хобби
# двух пользователей, и вычисляет процент совпадения. Использовать множества.


# def hobby(a, b):
#     a = set(a)
#     b = set(b)
#     c = a & b
#     return c, len(c) / len(a | b) * 100
#
# print(hobby(['хоккей', 'тв', 'футбол', 'шахматы', 'шахматы'], ['хоккей', 'тв', 'баскетбол', 'керлинг']))




