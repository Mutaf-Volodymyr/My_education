# def word_multiply(text: str, num: int) -> str:
#     return text * num
#
#
# print(type(word_multiply('Hello World', -1)))



from operator import itemgetter

def sort_dicts_by_key(dicts, sort_key):
    return sorted(dicts, key=itemgetter(sort_key))


d = [
    {'a': 1, 'b': 2, 'c': 1, 'd': 4},
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'a': 1, 'b': 2, 'c': 6, 'd': 4},
    {'a': 1, 'b': 2, 'c': 88, 'd': 4},
    {'a': 1, 'b': 2, 'c': 336, 'd': 4},
    {'a': 1, 'b': 2, 'c': 11, 'd': 4},
    ]



# Напишите генератор, который возвращает последовательность целых чисел, где каждое
# следующее больше предыдущего в 2 раза.

# def dupell(start):
#     while True:
#         yield start
#         start *= 2
#
# dupell_5 = dupell(5)
#
# for _ in range(10):
#     print(next(dupell_5))


# У вас есть текстовый файл, где каждая строка - имя человека. Написать программу,
# которая выводит следующее приветствие: “Привет, <имя 1, <имя 2,... <имя n> и добро
# пожаловать!ˮ. Программу реализовать с помощью генератора и суб-генератора,
# где субгенератор возвращает имена из файла, а основной генератор в нужный момент считывает и
# возвращает значения из суб-генератора.


# def generator_1(name_file):
#     with open(name_file, 'r', encoding='utf-8') as file:
#         yield 'Привет'
#         yield from (i.strip() for i in file)
#         yield 'и добро пожаловать!'
#
# gen = generator_1('names_.txt')
# print(*gen, sep=', ')


# 2. Напишите генератор, в который передаются строки разной длины и который возвращает
# строки фиксированной длины 7 символов. Если длина переданной строки больше 7
# символов, то возвращаются первые 7 символов. Если длина переданной строки меньше 7
# символов, то недостающие символы присоединяются к строке слева в виде нулей (“abcdˮ
# → “000abcdˮ).

# def generator_2(n):
#     word = yield
#     while True:
#         if len(word) == n:
#             word = yield word
#         elif len(word) > n:
#             word = yield word[:n]
#         elif len(word) < n:
#             word = yield (n - len(word)) * '0' + word
#
# result = generator_2(7)
# result.__next__()
# while True:
#     txt = input()
#     print(result.send(txt))
#     if txt == 'close':
#         result.close()
#         break



