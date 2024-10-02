from functools import partial
#
# mult_by_two = partial(lambda x, y: x * y, 2)
# result = mult_by_two(5)
# print(result)

# def say(a, b, c='!'):
#     print(a, b, c)
# say('Bye', 'Mike')
# say('Hello', 'world', c='.')
# new_say = partial(say, 'Hello', b='Jack')
# new_say()


# ФИБОНАЧИИИИИИИИИИИИИИИ!!!!!!!!!!!!!!!!!!!!!
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(10))


# def fib(n):
#     cache = {1: 1, 2: 1}
#     def fib_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = fib_rec(n - 2) + fib_rec(n - 1)
#             cache[n] = result
#         return result
#     return fib_rec(n)
#
# print(fib(10))


