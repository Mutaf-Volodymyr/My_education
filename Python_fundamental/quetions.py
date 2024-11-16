
# изменяемые обьекты и итераторы

# list_for_iter = [13, 200, 3, 40, 51, 66, 79, 78, 96, 10]
# iterator = iter(list_for_iter)
#
# print(next(iterator))
# list_for_iter[1] = 'hallo'
# print(next(iterator))
# del list_for_iter[0]
# print(next(iterator))






# не изменяемые обьекты и итераторы
# str_for_iter = '1234567890'
# iterator2 = iter(str_for_iter)
# print(next(iterator2))
# str_for_iter = str_for_iter.replace('2', 'R')
# print(next(iterator2))
# str_for_iter = str_for_iter[5:]
# print(next(iterator2))





# файлы и итераторы
# file = open('persons.csv', 'r')
# print(next(file), end='')
# input()
# for line in file:
#     print(line, end='')
# file.close()




#########
# file = open('persons.csv', 'r')
# print(next(file), end='')
# input()
# file.close()
# file = open('persons.csv', 'r')
# for line in file:
#     print(line, end='')
# file.close()





#########
# with open('persons.csv', 'r') as f:
#     print(next(f), end='')
#     input()
#     for line in f:
#         print(line, end='')





