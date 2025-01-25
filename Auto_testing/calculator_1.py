from decimal import Decimal

class Calculator:
    #Elena sum(self, a, b)
    def sum(self, a, b):
        a = Decimal(str(a))
        b = Decimal(str(b))
        return float(a + b)

    #Kirill sub(self, a, b)
    def sub(self, a, b):
        a = Decimal(str(a))
        b = Decimal(str(b))
        return float(a - b)

    # Oleksandr mul(self, a, b)
    def mul(self, a, b):
        a = Decimal(str(a))
        b = Decimal(str(b))
        return float(a * b)

    #Vladimir div(self, a, b)
    def division(self, a, b):
        if b == 0:
            return 'Деление на ноль запрещено!'
        if  type(a) not in (int, float):
            return 'Невалидное значение первого аргумента'
        if  type(b) not in (int, float):
            return 'Невалидное значение второго аргумента'
        a = Decimal(str(a))
        b = Decimal(str(b))
        return float(a / b)

    def average(self, *args):
        if not args:
            return 0
        return sum(args) / len(args)

    def len_gerlanda(self, nums: list[int]) -> int:
        result = 0
        iter1 = iter(nums)
        iter2 = iter(nums)
        iter2.__next__()
        for num1, num2 in zip(iter1, iter2):
            result += abs(num2 - num1)
        return result

a = Calculator()
print(a.len_gerlanda([7, 9, 10, 15, 24]))


