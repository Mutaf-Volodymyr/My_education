# Модуль functools
## Функция partial()
### Частичное применение функций — это техника, основанная на возможности возвращать функции из других функций.

#### Сигнатура функции следующая: 
    partial(func, *args, **kwargs)
Пример:
    
    from functools import partial
    
    def multiply(a, b):
        return a * b
    
    double = partial(multiply, 2)
    triple = partial(multiply, 3)

### Объекты, возвращаемые функцией partial()

Как уже было сказано выше, функция partial() возвращает специальные partial объекты, которые при вызове ведут себя как функции. Такие объекты содержат три полезных атрибута:

- `func` — исходная функция
- `args` — зафиксированные позиционные аргументы (тип tuple)
- `keywords` — зафиксированные именованные аргументы (тип dict)

Приведенный ниже код:

    from functools import partial
    
    def pretty_print(text, symbol, count):
        print(symbol * count)
        print(text)
        print(symbol * count)
    
    star_pretty_print = partial(pretty_print, 'Hi!!!', symbol='*')
    
    star_pretty_print(count=7)
    
    print(star_pretty_print.args)
    print(star_pretty_print.keywords)
    
    star_pretty_print.func('Исходная функция', symbol='~', count=20)
выводит:

    *******
    Hi!!!
    *******
    ('Hi!!!',)
    {'symbol': '*'}
    ~~~~~~~~~~~~~~~~~~~~
    Исходная функция
    ~~~~~~~~~~~~~~~~~~~~

## Функция update_wrapper()
#### С помощью функции update_wrapper() из модуля functools можно скопировать и добавить атрибуты __name__ и __doc__ из исходной функции в partial объект.

    from functools import partial, update_wrapper
    
    def multiply(a, b):
        '''Функция перемножает два числа и возвращает вычисленное значение.'''
        return a * b
    
    double = partial(multiply, 2)
    
    update_wrapper(double, multiply)   # копируем информацию из функции multiply в partial объект double
    
    print(double.__name__)
    print(double.__doc__)






















