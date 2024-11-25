# Существует функция coffee(), которая варит кофе и если ее вызвать, то она печатает “кофе”.
# Декорировать эту функцию так, чтобы можно было варить кофе с сахаром, молоком или и тем и другим.
# Вызов декорируемой функции должен печатать, с чем кофе сварено. Сварить кофе с
# двойной порцией сахара и молока. Сварить двойной кофе.

import functools


def coffe_with(milk_qty=0, suger_qty=0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if milk_qty or suger_qty:
                res += ' with'
                if milk_qty:
                    res += f" {milk_qty} milk"
                if suger_qty:
                    res += f" {suger_qty} suger"
            return res

        return wrapper

    return decorator


@coffe_with(milk_qty=1, suger_qty=2)
def make_drink(drink='coffee'):
    return drink


print(make_drink('tee'))


# Реализовать декоратор lru_cache, который сохраняет до последних 3 вызовов функции
# и если она была повтовно и есть сохраненные результаты, то вернуть результаты


import functools


def lru_cache(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]
        value = func(*args, **kwargs)
        cache[key] = value
        return value
    return wrapper
