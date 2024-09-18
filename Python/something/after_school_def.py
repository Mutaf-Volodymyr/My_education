# def f1():
#     a = 5
#
# def f2():
#     a = 6


def my_function_2(*, num_list:list) ->tuple:
    return sum(num_list), min(num_list), max(num_list)