# Напишите программу, которая принимает список слов от пользователя и использует
# генераторное выражение (comprehension) для создания нового списка, содержащего только те слова,
# которые начинаются с гласной буквы. Затем программа должна использовать функцию map,
# чтобы преобразовать каждое слово в верхний регистр. В результате программа должна
# вывести новый список, содержащий только слова, начинающиеся с гласной
# буквы и записанные в верхнем регистре.

# Очень не оптимизировано, но по условию:
vowels = 'AEIOUYaeiouy'
text = input().split()
res = list(map(str.upper, (word for word in text if word[0] in vowels)))
print(res)

# Оптимизировано, но не по условию:
res_optim = [word.upper() for word in text if word[0] in vowels]
print(res_optim)



# Напишите программу, которая принимает список чисел от пользователя и использует функцию
# reduce из модуля functools, чтобы найти произведение всех чисел в списке.
# Затем программа должна использовать функцию itertools.accumulate
# для накопления произведений чисел в новом списке.
# В результате программа должна вывести список, содержащий накопленные произведения.

from operator import mul
from itertools import accumulate, tee
from functools import reduce

list_of_num1, list_of_num2 = tee(map(float, input().split()))

print(reduce(mul, list_of_num1))
print(list(accumulate(list_of_num2, mul)))




