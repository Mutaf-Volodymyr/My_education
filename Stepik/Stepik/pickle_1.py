# Найдите и исправьте ошибки, допущенные в приведенной ниже программе, чтобы она сериализовала словарь
# dogs и записала результат в файл dogs.pkl.

# import pickle
# dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}
# with open('pickle_1/dogs.pkl', mode='wb') as file:
#     pickle.dump(dogs, file)


num1 = 100
num2 = 100

num3 = 10**33
num4 = 10**33

print(num1 is num2, num1 == num2)
print(num3 is num4, num3 == num4)

# -------------------------

s1 = 'b' * 4096
s2 = 'b' * 4096

s3 = 'b' * 5000
s4 = 'b' * 5000

print(s1 is s2)
print(s3 is s4)