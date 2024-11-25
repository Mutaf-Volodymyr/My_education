# 1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об
# ошибке, если переданы аргументы неправильного типа.
# Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.


def validate_args(*args, **kwargs):
    position_args = args
    names_args = kwargs.items()

    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, j in zip(args, position_args):
                if type(i) != j:
                    raise TypeError(f'Position argument {i} has wrong type: {type(i)}. The right type: {j}')
            for i, j in zip(sorted(kwargs.items()), sorted(names_args)):
                if type(i[1]) != j[1]:
                    raise TypeError(f'Named argument <{i[0]}> has wrong type: {type(i[1])}. The right type: {j[1]}')

            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


@validate_args(age=int, name=str)
def greet2(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


# greet(25, "Анна")  # Все аргументы имеют правильные типы
# greet("25", "Анна")  # Возникнет исключение TypeError
# greet2(age=25, name="Анна")  # Все аргументы имеют правильные типы
# greet2(age="25", name="Анна")  # Возникнет исключение TypeError

# Ожидаемый вывод:
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.


# 2. Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>,
# Результат: <результат>". Используйте модуль logging для записи в лог-файл.
import functools


def log_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('log.txt', 'a') as f:
            text = f'Arguments: {args}, {kwargs} Result: {value}\n'
            f.write(text)
        return value

    return wrapper


@log_args
def add(a, b):
    return a + b


add(2, 3)
add(5, 7)
