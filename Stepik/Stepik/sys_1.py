# Напишем программу, которая дублирует каждую введённую пользователем строку.
# import sys
#
# for line in sys.stdin:
#     print(line + 'hallo', end='')



# С помощью потока ввода (sys.stdin) можно в одну строчку кода прочитать весь пользовательский ввод в список.

# import sys
# data = [line.strip() for line in sys.stdin]
# или
# data = list(map(str.strip, sys.stdin))

# Кроме того, можно считать все строки из итератора
# import sys
# data = sys.stdin.readlines()
# или
# data = sys.stdin.read()

# import sys
# sys.stdout.write(str(17))     # преобразуем данные в строку

# Напишите программу, которая принимает произвольное количество строк и в
# каждой введенной строке располагает все символы в обратном порядке.
# import sys
# text = [line.strip() for line in sys.stdin]
# print(*map(lambda x:x[::-1], text), sep='\n')

# Дана последовательность дат. Напишите программу,
# которая выводит количество дней между максимальной и минимальной датами данной последовательности.
# import sys
# from datetime import date
# dates = [date.fromisoformat(d.strip()) for d in sys.stdin]
# delta = max(dates) - min(dates)
# print(delta.days)

# Анри и Дима, имея на руках ящик с бесконечным количеством носков, решили сыграть в игру.
# Ребята по очереди достают из ящика произвольное количество носков, и после неопределенного
# числа ходов игра заканчивается. Если тот, кто сделал последний ход, вытащил четное количество
# носков — он побеждает, в противном случае проигрывает.
# Напишите программу, которая определяет победителя в данной игре, если первый ход делает Анри.

# import sys
# count = 0
# players = ('Дима', 'Анри')
# for num in sys.stdin:
#     count += 1
# count %= 2
# if int(num) % 2 == 0:
#     print(players[count])
# else:
#     print(players[int(not bool(count))])


# Дан список чисел, каждое из которых — рост очередного ученика онлайн-школы BEEGEEK. Напишите программу,
# которая определяет рост самого низкого и самого высокого учеников, а также средний рост среди всех учеников.

# import sys
# alles = [int(i.strip()) for i in sys.stdin]
# if alles:
#     print(f'Рост самого низкого ученика: {min(alles)}\n'
#           f'Рост самого высокого ученика: {max(alles)}\n'
#           f'Средний рост: {sum(alles) / len(alles)}')
# else:
#     print('нет учеников')


# Дан блок кода на языке Python. Напишите программу, которая определяет количество строк в данном коде, которые
# содержат в себе только комментарии. Если в строке помимо комментария имеется что-то еще, то такую строку учитывать не нужно.
# import sys
# print(sum([1 for i in sys.stdin if i.strip().startswith('#')]))

# Дан блок кода на языке Python. Напишите программу, которая удаляет все строки в данном коде, которые содержат в себе только комментарии.
# Если в строке помимо комментария имеется что-то еще, то такую строку учитывать не нужно.
# import sys
# print(*[i for i in sys.stdin if not i.strip().startswith('#')],sep='', end='')

# По чатам одного немалоизвестного мессенджера начали появляться новости сомнительного содержания. Оказалось,
# что некий молодежный клуб решил подшутить, распространяя всякие глупости. Однако подобное хулиганство мешает
# доверчивым людям, особенно пенсионного возраста, поэтому группа независимых программистов решила разработать бота,
# который мог бы оценить степень достоверности новости, а также отнести её к какой-либо категории.
# Напишите программу, которая выводит все новости заданной категории, располагая их по возрастанию степени достоверности.
# Формат входных данных
# На вход программе подается произвольное количество строк, в каждой строке, кроме последней, записана новость,
# категория, к которой она относится, и ее достоверность в следующем формате:
# <новость> / <категория> / <достоверность>
# В последней строке подается одиночная категория.
# Программа должна вывести все новости, которые относятся к введенной категории.
# Новости должны быть расположены в порядке возрастания степени достоверности, а при
# совпадении степеней достоверности — в лексикографическом порядке самих новостей.

# import sys
# news = [i.strip().split(' / ') for i in sys.stdin]
# tema = news.pop()[0]
# news = filter(lambda x: tema in x, news)
# news = sorted([[float(i[2]), i[0]] for i in news])
# [print(i[1]) for i in news]

# Дана последовательность дат. Напишите программу, которая определяет, в каком порядке расположены даты в данной последовательности.
# Формат входных данных
# На вход программе подается произвольное количество строк (две или более), в каждой строке записана дата в формате DD.MM.YYYY.
# Формат выходных данных
# Программа должны вывести текст:
# ASC, если даты в введенной последовательности расположены строго в порядке возрастания
# DESC, если даты в введенной последовательности расположены строго в порядке убывания
# MIX, если даты в введенной последовательности расположены ни в порядке возрастания, ни в порядке убывания

#
# import sys
# from datetime import datetime
#
# news = [datetime.strptime(i.strip(), '%d.%m.%Y') for i in sys.stdin]
# if len(news) != len(set(news)):
#     print('MIX')
# elif news == list(sorted(news)):
#     print('ASC')
# elif news == list(sorted(news, reverse=True)):
#     print('DESC')
# else:
#     print('MIX')


# Дана последовательность целых чисел. Напишите программу, которая определяет, является ли
# данная последовательность прогрессией, и если да, то определяет её вид.
# Формат входных данных
# На вход программе подается произвольное количество строк (не менее трёх), в каждой строке записано
# натуральное число — очередной член последовательности.

# import sys
# p = [int(i.strip()) for i in sys.stdin]

# res = ('Арифметическая прогрессия', 'Геометрическая прогрессия', 'Не прогрессия')
# flag = 2
# a = p[1] - p[0]
# for i in range(2, len(p)):
#     if p[i] - p[i-1] != a:
#         break
# else:
#     flag = 0
#
# a = p[1] / p[0]
# for i in range(2, len(p)):
#     if p[i] / p[i - 1] != a:
#         break
# else:
#     flag = 1
# print(res[flag])






