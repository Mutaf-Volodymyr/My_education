import asyncio


# async def task_one():
#     await asyncio.sleep(10)
#     print("Task one complete")
#
#
# async def task_two():
#     await asyncio.sleep(10)
#     print("Task two complete")
#
#
# async def main():
#     await task_one()
#     await task_two()
#
#
# asyncio.run(main())

# Создание задачи


# import asyncio
#
# async def task1():
#     await asyncio.sleep(10)
#     print("Задача 1 завершена")
#
# async def task2():
#     await asyncio.sleep(20)
#     print("Задача 2 завершена")
#
# async def task3():
#     for i in range(1, 20):
#         await asyncio.sleep(1)
#         print(i)
#
#
# async def main():
#     task1_obj = asyncio.create_task(task1())
#     task2_obj = asyncio.create_task(task2())
#     task3_obj = asyncio.create_task(task3())
#
#     await task1_obj
#     await task2_obj
#     await task3_obj
#
# asyncio.run(main())

# Отмена задачи

# import asyncio
#
#
# async def my_coroutine():
#     try:
#         print("Начало выполнения задачи")
#         await asyncio.sleep(5)
#         print("Задача выполнена")
#     except asyncio.CancelledError:
#         print("Задача была отменена")
#
#
# async def main():
#     task = asyncio.create_task(my_coroutine())
#
#     # Начало выполнения задачи и ожидание 2 секунды
#     await asyncio.sleep(2)
#
#     # Отмена задачи
#     task.cancel()
#
#     await task
#
#
# asyncio.run(main())



# Создайте две корутины:
#
# Корутина amount: принимает два параметра с типом int и выводит их сумму с использованием функции print
# Корутина main: дважды запрашивает ввод данных с помощью функции input . После получения данных она должна
# обернуть корутину amount в задачу, передать ей полученные данные, заплонировать выполнение задачи и дождаться ее завершения

# async def amount(a:int, b: int) -> None:
#     print(a+b)
#
#
# async def main():
#     a, b = int(input()), int(input())
#     new_task = asyncio.create_task(amount(a, b))
#
#     await new_task
#
#
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())



# Создайте две корутины:
#
# Корутина task:
# • принимает два параметра:
#     — число с типом int
#     — текст с типом str
# • вызывает корутину sleep из библиотеки asyncio, передавая ей числовой параметр
# • выводит полученный текст с помощью функции print
#
# Корутина main:
# • запрашивает четыре ввода данных с помощью функции input :
#     — первые два содержат числа (необходимо привести к типу int)
#     — следующие два содержат произвольный текст
# • создает первую задачу, оборачивая корутину task и передает первое полученное число (1ый ввод) и первый полученный текст (3ий ввод)
# • создает вторую задачу, оборачивая корутину task и передает второе полученное число (2ой ввод) и второй полученный текст (4ый ввод)
# • планирует обе задачи к выполнению и дожидается их завершения

# async def task(a:int, b: str):
#     await asyncio.sleep(a)
#     print(b)
#
#
# async def main():
#     a, b = int(input()), int(input())
#     x, y = input(), input()
#
#     task1 = asyncio.create_task(task(a, x))
#     task2 = asyncio.create_task(task(b, y))
#
#     await task1
#     await task2
#
#
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())




# Корутина task:
# • принимает параметр с типом int
# • вызывает корутину sleep и передает ей полученный параметр
# • возвращает строку Ожидание parameter секунд завершено , где parameter — полученный параметр
# Корутина main:
# • получает числовое значение с помощью функции input — количество создаваемых задач
# • создает полученное количество задач, оборачивая корутину task, где для каждой задачи аргумент получается отдельным вызовом input
# • запускает задачи, используя gather
# • ожидает завершения всех задач и выводит список результатов

# async def task(a:int):
#     await asyncio.sleep(a)
#     return f'Ожидание {a} секунд завершено'
#
# async def main():
#    b = [asyncio.create_task(task(int(input()))) for _ in range(int(input()))]
#    res = await asyncio.gather(*b)
#    print(res)
#
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())




# Создайте две корутины:
#
# Корутина task:
# • принимает параметр с типом int
# • вызывает корутину sleep и передает ей полученный параметр
# • возвращает полученный параметр
# Корутина main:
# • получает числовое значение с помощью функции input — количество создаваемых задач
# • получает числовое значение с помощью функции input — значение аргумента timeout для функции wait
# • создает полученное количество задач, оборачивая корутину task, где для каждой задачи аргумент получается отдельным вызовом input
# • запускает задачи, используя wait с полученным таймаутом
# • ожидает завершения всех задач / срабатывания таймаута
# • печатает Завершено N задач , где N — количество завершенных задач
# • печатает Не успели завершиться N задач , где N — количество незавершенных задач


async def task(a:int):
    await asyncio.sleep(a)
    return f'Ожидание {a} секунд завершено'

async def main():
    c = int(input())
    t = int(input())
    b = [asyncio.create_task(task(int(input()))) for _ in range(c)]
    done, pending = await asyncio.wait(b, timeout=t)
    print(f'Завершено {len(done)} задач')
    print(f'Не успели завершиться {len(pending)} задач')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())