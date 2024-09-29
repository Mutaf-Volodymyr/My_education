## Основные типы исключений

### Что касается типов исключений, наибольший интерес с практической точки зрения представляют следующие:

- `IndexError`: возникает, когда индекс (например, для элемента списка) указан неправильно (выходит за границы допустимого диапазона)
- `KeyError`: возникает при неверно указанном ключе словаря
- `NameError`: возникает, если не удается найти переменную с некоторым названием
- `SyntaxError`: возникает при наличии в исходном коде синтаксических ошибок
- `TypeError`: возникает при несоответствии типов, когда для обработки требуется значение определенного типа, а передается значение другого типа
- `FileNotFoundError`: возникает при открытии несуществующего файла
- `ValueError`: возникает, когда в функцию передается аргумент с неподдерживаемым значением
- `ZeroDivisionError`: возникает при попытке выполнить деление на ноль

## Общий шаблон инструкции try-except

    try:
        контролируемый код
    except тип_ошибки_1:
        код обработки ошибки (исключения)
    except тип_ошибки_2:
        код обработки ошибки (исключения)
    ...
    except тип_ошибки_n:
        код обработки ошибки (исключения)
    else:
        код для случая, если ошибки не было
    finally:
        код, который выполняется всегда


## В Python присутствует строгая иерархия исключений, вершиной которой является тип BaseException.
### Дерево встроенных исключений выглядит так:

    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
               +-- ModuleNotFoundError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning

Тип Exception – базовый класс для большинства встроенных в Python исключений. Именно его, а не BaseException, необходимо наследовать при создании пользовательского класса исключения.
Для проверки родства классов исключений можно использовать встроенную функцию ` issubclass() `, которая указывает на то, является ли некоторый класс потомком указанного класса или нет.

Важно помнить, что если у нас используется несколько блоков except, то первыми нужно указывать наиболее конкретные. Иначе мы можем оказаться в ситуации вроде этой:

    try:
        nums = [10, 5, 20, 25]
        print(nums[100])
    except Exception:
        print('Произошла ошибка!')
    except (KeyError, IndexError):
        print('Ошибка связанная с индексом!')

Здесь первый блок except отлавливает вообще все исключения, ведь любое конкретное исключение наследуется от типа Exception. Второй блок except не имеет шанса хоть раз быть выполненным.

### Если нужен доступ к сгенерированному исключению как к объекту, то используется специальный синтаксис.

Приведенный ниже код:

    try:
        nums = [10, 5, 20, 25]
        print(nums[100])
    except (KeyError, IndexError) as err:    # записываем сгенерированное исключение в переменную err
        print(err)
        print(type(err))
выводит:

    list index out of range
    <class 'IndexError'>
В данном примере в переменную err попадает объект типа IndexError.

Посмотреть все атрибуты объекта сгенерированного исключения можно с помощью встроенной функции dir().

Приведенный ниже код:

    try:
        print(1 / 0)
    except ZeroDivisionError as err:
        print(dir(err))
выводит:

    ['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
    '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
    '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', 
    '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'with_traceback']


Если при обработке всех исключений одним блоком except мы хотим получить доступ к объекту исключения, то нужно явно указать его тип.

    try:
        х = 1 / 0
    except Exception as err:
        print(err)


Для получения информации об исключении можно воспользоваться функцией `exc_infо()` из модуля `sys`. Данная функция возвращает кортеж из трех значений: типа исключения, значения и объекта с трассировочной информацией об исключении, которое в данный момент обрабатывается.

Приведенный ниже код:

    from sys import exc_info
    
    try:
        х = 1 / 0
    except Exception as err:
        print(exc_info())
выводит:

    (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001BEEF80E840>)
Преобразовать эти значения в удобочитаемый вид позволяет модуль `traceback`.


## Возбуждение исключений
Для возбуждения исключения используется оператор `raise`. В качестве аргумента оператор `raise` использует экземпляр класса, унаследованного от `Exception`.

    try:
        raise IndexError('ошибочка')             # возбуждение исключения вручную
    except Exception as err:
        print(err)
        print(type(err)) 

Оператор возбуждения исключений raise имеет несколько вариантов формата:

- raise <экземпляр класса>
- raise <название класса>
- raise <экземпляр или название класса> from <объект исключения>
- raise