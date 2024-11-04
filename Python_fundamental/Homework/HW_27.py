
# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только
# четных чисел из списка, используя функциональные подходы (например, map, filter и reduce).
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72

print(sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, map(int, input().split())))))



# Напишите функцию, которая принимает на вход список функций и значение, а затем применяет композицию этих
# функций к значению, возвращая конечный результат.


def compose_functions(funcs:list, num:int) -> int:
    result = num # что бы не изменять num
    for func in funcs:
        result = func(result)
    return result


add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3
functions = [add_one, double, subtract_three]
print(compose_functions(functions, 12))

