# def add_dollar_prefix(func):
#     def wrapper():
#         result = str(func())
#         return '$' + result
#
#     return wrapper
#
# @add_dollar_prefix
# def get_price(item):
#     prices = {'comic book': 5, 'puzzle': 15}
#     return prices[item]
#
# print(get_price('comic book'))


# ---------------- АРГУМЕНТЫ

#
# def del_first_char(func):
#     def wrapper():
#         return func()[1:]
#
#     return wrapper
#
#
# @del_first_char
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())


# def add_dollar_prefix(func):
#     def wrapper(*args, **kwargs):
#         result = str(func(*args, **kwargs))
#         return '$' + result
#
#     return wrapper
#
# @add_dollar_prefix
# def get_price(item, discount=0):
#     prices = {'comic book': 5, 'puzzle': 20}
#     return prices[item] - discount
#
# print(get_price('puzzle', discount=4))

########################### АААААА!!!!!!
# Реализуйте декоратор sandwich, который выводит тексты:
#
# ---- Верхний ломтик хлеба ----
# ---- Нижний ломтик хлеба ----
# до и после вызова декорируемой функции соответственно.
#
# def sandwich(func):
#     def wrapper(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         s = func(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')
#         return s
#
#     return wrapper
#
# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))
#
# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
#
#
# @sandwich
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())

###########################
# Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

# def do_twice(func):
#      def wrapper(*args, **kwargs):
#          func(*args, **kwargs)
#          return func(*args, **kwargs)
#
#      return wrapper
###########################
# Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func в обратном порядке.

# def reverse_args(func):
#     def wrapper(*args, **kwargs):
#         args = list(args)[::-1]
#         return func(*args, **kwargs)
#
#     return wrapper


###########################
# Реализуйте декоратор exception_decorator, который возвращает
#
# кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила свою работу без ошибок,
#   где value — возвращаемое значение декорируемой функции
# кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка
# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             value = func(*args, **kwargs)
#             return (value, 'Функция выполнилась без ошибок')
#         except:
#             return (None, 'При вызове функции произошла ошибка')
#
#     return wrapper


###########################
# # Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.
# # Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
# # TypeError, если аргумент не является целым числом
# # ValueError, если аргумент является целым числом, но отрицательным или равным нулю
#
# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         for i in list(args) + list(kwargs.values()):
#             if type(i) != int:
#                 return TypeError
#             elif i <= 0:
#                 return ValueError
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


###########################
# def up_print(func):
#     def wrapper(*args, **kwargs):
#         args = [i.upper() if type(i) == str else i for i in args]
#         kwargs = {k:v.upper() if type(v) == str else v for k,v in kwargs.items()}
#         func(*args, **kwargs)
#     return wrapper
#
#
# print = up_print(print)
#
# print('hi', 'there', end='!')

###########################
# Реализуйте декоратор square, который возводит возвращаемое значение декорируемой функции во вторую степень.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# import functools
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) ** 2
#     return wrapper

########################### почему я должен использовать raise????
# Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции
# принадлежит типу str. Если возвращаемое значение принадлежит какому-либо другому типу,
# декоратор должен возбуждать исключение TypeError.
#Также декоратор должен сохранять имя и строку документации декорируемой функции.

# import functools
# def returns_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         for i in list(args) + list(kwargs.values()):
#             if type(i) != str:
#                 raise TypeError
#         res = func(*args, **kwargs)
#         if type(res) != str:
#             raise TypeError
#         return res
#     return wrapper




###########################
# Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения,
# а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:
#
# TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
# TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# import functools
# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}\n'
#               f'TRACE: возвращаемое значение {func.__name__}(): {repr(result)}')
#         return result
#     return wrapper


###########################
# Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:
    # string — произвольная строка
    # to_the_end — булево значение, по умолчанию равное False
# Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. Если to_the_end имеет значение True,
# строка string добавляется в конец, если False — в начало.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# import functools
# def prefix(string, to_the_end=False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             match to_the_end:
#                 case True: result = result + string
#                 case False: result = string + result
#             return result
#         return wrapper
#     return decorator



###########################
# Реализуйте декоратор make_html(), который принимает один аргумент:
# tag — HTML-тег, например, del
# Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# import functools
# def make_html(tag):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#             return result
#         return wrapper
#     return decorator


###########################
# Реализуйте декоратор repeat, который принимает один аргумент:
# times — натуральное число
# Декоратор должен вызывать декорируемую функцию times раз.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# import functools
# def repeat(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times-1):
#                 func(*args, **kwargs)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator



###########################
# Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:

    # start — неотрицательное целое число
    # end — неотрицательное целое число
    # char — одиночный символ, по умолчанию равный точке .
# Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все символы в
# диапазоне индексов от start (включительно) до end (не включительно) на символ char.

# import functools
# def strip_range(start:int, end:int, char:str='.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = list(func(*args, **kwargs))
#             l = len(result)
#             for i in range(start, end):
#                 if i >= l:
#                     break
#                 result[i] = char
#             return ''.join(result)
#         return wrapper
#     return decorator


###########################
# Реализуйте декоратор returns, который принимает один аргумент:
#
# datatype — тип данных
# Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype.
# Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# import functools
# def returns(datatype):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if not isinstance(result, datatype):
#                 raise TypeError
#             return result
#         return wrapper
#     return decorator


###########################
# Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов,
# каждый из которых является типом данных.
# Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат
# одному из этих типов. Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# import functools
# def takes(*args_t):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for el in list(args) + list(kwargs.values()):
#                 if type(el) not in args_t:
#                     raise TypeError
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


###########################
# Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов и устанавливает
# их в качестве атрибутов декорируемой функции. Названием атрибута должно являться имя аргумента, значением атрибута — значение аргумента.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# import functools
# def add_attrs(**kwargs_atr):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#
#         for k, v in kwargs_atr.items():
#             wrapper.__dict__[k] = v
#         return wrapper
#
#     return decorator


###########################
# Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:
# Исключение <тип исключения> обработано
# если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.
# Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.


# import functools
# def ignore_exception(*args_error):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 res =func(*args, **kwargs)
#             except Exception as e:
#                 if type(e) in args_error:
#                     print(f'Исключение {type(e).__name__} обработано')
#                 else:
#                     raise e
#             else:
#                 return res
#         return wrapper
#
#     return decorator





###########################
# Реализуйте декоратор retry, который принимает один аргумент:
# times — натуральное число
# Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка.
# Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, после чего должен возбуждать исключение
# MaxRetriesException.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.


# import functools
#
# class MaxRetriesException(Exception):
#     pass
#
# def retry(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 try:
#                    res =  func(*args, **kwargs)
#                 except:
#                     pass
#                 else:
#                     return res
#             raise MaxRetriesException
#
#         return wrapper
#
#     return decorator


