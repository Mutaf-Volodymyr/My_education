# 😀😄😁😆😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨😫😩🥺😢😭😤😠😡
# Dont be so sad!
from turtledemo.sorting_animate import partition

# new_abc = 🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩
# I love Python =)

# import string
# trantab = str.maketrans(string.ascii_lowercase, new_abc)
# text = input().lower()
# print (text.translate(trantab))




#
# import string
# new_abc = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩'
# tran_tab = str.maketrans(string.ascii_lowercase, new_abc)
# my_tuple = ('Hello world!', '😁')
# print(my_tuple[0].lower().translate(tran_tab), my_tuple[1], sep='')


# # 1. Дан массив целых чисел. Написать функцию, которая вернет true,
# # если 6 является первым или последним элементом массива,
# # false в противном случае. Массив минимальной длины 1.
#
# def my_function(my_list):
#     return my_list[0] == my_list[-1]
#
#
# print(my_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))
# print(my_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#
#
# # 2. Дано два массива целых чисел. Написать функцию, которая
# # возвращает true, если их первые или последние элементы равны.
# # Оба массива минимальной длины 1.
#
# def my_function_2(my_list1, my_list2):
#     a = my_list1[0] == my_list2[0], my_list1[-1] == my_list2[-1]
#     return any(a)
#
#
# print(my_function_2([1, 2, 3, 4], [0, 2]))
# print(my_function_2([1, 2, 3, 4], [1, 2]))
#
#
# # 3. Дан массив целых чисел длины 3. Написать функцию,
# # которая возвращает массив “повернутый влево”:
# # [1, 2, 3] -> [2, 3, 1], [5, 11, 9] -> [11, 9, 5]
#
# def my_function_3(my_list1):
#     return [my_list1[1], my_list1[2], my_list1[0]]
#
# print(my_function_3([5, 11, 9]))
#
#
# # 4. Дан массив целых чисел длины 1 и более. Написать функцию,
# # которая возвращает массив длины 2, состоящих из первого
# # и последнего элемента входного массива.
# # {1, 2, 3} -> {1, 3}, {7, 4, 6, 2} -> {7, 2}
#
# def my_function_4(my_list1):
#     return [my_list1[0], my_list1[-1]]
#
# print(my_function_4([5, 11, 9]))
#
# print('-' * 15)

# 5. Напишите функцию, которая вернет количество четных чисел в
# данном массиве.

# my_list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(len(list(filter(lambda x: x % 2 == 0, my_list_5))))


# 6. Напишите функцию, которая возвращает сумму элементов массива
# и возвращает 0, если массив пустой. Так как число 13 приносит неудачу,
# функция не должна учитывать число 13 и последующие за ним числа в массиве.
# {1, 2, 2, 1} -> 6, {0, 2, 2, 3, 13} -> 7, {1, 2, 13, 2, 1} -> 3

# def my_function_6(my_list):
#     result = []
#     for i in my_list:
#         if i == 13:
#             break
#         result.append(i)
#     return sum(result)
#
# print(my_function_6([]))


# 8. Поменяйте предыдущую задачу так, чтобы функция возвращала true если в
# массиве стоят рядом два любых одинаковых элемента.

# def my_function_8(my_list):
#     for i in range(len(my_list)-1):
#         if my_list[i] == my_list[i+1]:
#             return True
#     return False

# def my_function_8(a):
#     return any([a[i] == a[i+1] for i in range(len(a)-1) if a[i] == a[i+1]])
#
#
# print(my_function_8([1, 2, 1, 2]))
# print(my_function_8([1, 2, 2]))


# 9. Дан список чисел. Выведите значение наибольшего
# элемента в списке, а затем индекс этого элемента в
# списке. Если наибольших элементов несколько,
# выведите индекс первого и последнего из них.

def my_function_9(a):
    res_num = max(a)
    first = a.index(res_num)
    second = len(a) - a[::-1].index(res_num) - 1
    return res_num, *sorted({first, second})

print(my_function_9([1, 6, 1, 6, 7, 4, 5, 6, 4, 1]))
print(my_function_9([1, 6, 1, 4, 5, 6]))



# 10. Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.
# {1, 2, 2, 3, 3, 3} -> 3, {1 1 1 1 1} -> 1




























