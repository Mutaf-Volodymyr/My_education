# Дана строка. При решении нельзя использовать циклы.
# a. Сначала выведите третий символ этой строки.
# b. Во второй строке выведите предпоследний символ этой строки.
# c. В третьей строке выведите первые пять символов этой строки.
# d. В четвертой строке выведите всю строку, кроме последних двух символов.
# e. В пятой строке выведите все символы с четными индексами (считая, что
# индексация начинается с 0, поэтому символы выводятся начиная с первого).
# f. В шестой строке выведите все символы с нечетными индексами, то есть начиная со
# второго символа строки.
# g. В седьмой строке выведите все символы в обратном порядке.
# h. В восьмой строке выведите все символы строки через один в обратном порядке,
# начиная с последнего.
# i. В девятой строке выведите длину данной строки.
#
# text = input()
# print(text[2])
# print(text[-1])
# print(text[:5])
# print(text[:-2])
# print(text[::2])
# print(text[1::2])
# print(text[::-1])
# print(text[::-2])
# print(len(text))

# 2. Напишите программу, которая печатает ценник по параметрам: “The price of <product> is
# “Xˮ Euroˮ. В строке <product> и <X> - параметры. Убедитесь, что цена выводится в Евро с
# центами (не более двух знаков после запятой).
#
# product = input()
# price = float(input())
# print(f'The price of {product} is {price:.2f} Euro')

# 3. Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней
# слов. Используйте для решения задачи метод count.

# text = input()
# print(text.count(' ') + 1)


# 4. Напишите программу, которая считает вхождение заданной подстроки в заданную строку.
# Например, для подстроки “abˮ и строки “Abrakadabraˮ программа напечатает 2.

# text = input().lower()
# print(text.count(input().lower()))

# 5. Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку. При решении этой задачи не стоит пользоваться
# циклами и инструкцией if.

# text = input()
# i = text.find(' ')
# print(text[i+1:] + ' ' + text[:i])
# print(*text.split()[::-1])


# 6. Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс ее первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите. При решении этой задачи
# не стоит использовать циклы.

# text = input()
# i = text.find('f')
# i_2 = text.rfind('f')
# if i == i_2 and i != -1:
#     print(i)
# elif i != i_2:
#     print(i, i_2)

# 7. Дана строка. Замените в этой строке все цифры 1 на слово one.
# text = input()
# print(text.replace('1', 'one'))

# 8. Есть строка `"<248>"`. Напишите программу,
# которая выведет на экран произведение чисел этой строки.

# text = input().strip('"<>')
# i = 0
# total = 1
# print(text)
# while i < len(text):
#     total *= int(text[i])
#     i += 1
# print(total)

# 9.
# Пользователь вводит строку. Напишите программу, которая разрежет строку пополам,
# переставит эти части местами и выведет результат на экран.

# text = input()
# i = len(text) // 2
# print(text[i:] + text[:i])











