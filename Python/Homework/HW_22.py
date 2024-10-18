# 1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

from time import sleep
try:
    with open('123.txt', 'r', encoding='utf-8') as f:
        for line in f:
            a, b = [int(i) for i in line.strip().split(' ')]
            if a < 0 or b < 0:
                raise ValueError
            print(a / b)
except FileNotFoundError:
    print('нет такого файла')
except ValueError:
    print('одно из чисел имеет отрицательное значение')
except ZeroDivisionError:
    print('Только не деление на ноль!!!!')
else:
    print('Процесс успешно завершен')
finally:
    print('Ваш компьютер взорвется через:')
    for i in [5, 4, 3, 2, 1 , 0.5, 0.25]:
        print(i)
        sleep(1)
    print('БАБАХ')




# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами
# (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для обработки исключений
# и закрытия файла в блоке finally.

try:
    file = open('123.txt', 'r', encoding='utf-8')
    for line in f:
        a, b = [int(i) for i in line.strip().split(' ')]
        if a < 0 or b < 0:
            raise ValueError
        print(a / b)
except FileNotFoundError:
    print('нет такого файла')
except ValueError:
    print('одно из чисел имеет отрицательное значение')
except ZeroDivisionError:
    print('Только не деление на ноль!!!!')
else:
    print('Процесс успешно завершен')
    file.close()





