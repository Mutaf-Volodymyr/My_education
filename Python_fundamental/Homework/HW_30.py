# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади прямоугольника и calculate_perimeter()
# для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
#
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем,
# его площадь и периметр.



class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.height

    def __str__(self):
        return f'rectangle_object (width: {self.width}, height: {self.height})'

    def __repr__(self):
        return (f'rectangle_object \n'
                f'\t(width: {self.width}, height: {self.height})\n'
                f'\t(area: {self.calculate_area()}, perimeter: {self.calculate_perimeter()})')


first_rectangle = Rectangle(12.5, 46.3)
print(first_rectangle.calculate_area())
print(first_rectangle.calculate_perimeter())
print(first_rectangle)
print(repr(first_rectangle))

# 2. Создайте класс BankAccount для представления банковского счета.
# Класс должен иметь атрибуты account_number (номер счета) и balance (баланс),
# а также методы deposit() для внесения денег на счет и withdraw()
# для снятия денег со счета. Затем создайте экземпляр класса BankAccount,
# внесите на счет некоторую сумму и снимите часть денег.
# Выведите оставшийся баланс. Не забудьте предусмотреть вариант,
# при котором при снятии баланс может стать меньше нуля.
# В этом случае уходить в минус не будем, вместо чего будем возвращать
# сообщение "Недостаточно средств на счете".

from datetime import date
from random import randint


class NotEnoughMoney(Exception):
    pass


class Person:
    def __init__(self, name: str, surname: str, birth_date: date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.working = False

    def __str__(self):
        return f'{self.name} {self.surname} - {self.birth_date}'

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def is_adulthood(self):
        return self.get_age() >= 18

    def get_all_accounts(self):
        return BankAccount.list_accounts.get(self, None)

    def get_all_money(self):
        list_accounts = self.get_all_accounts()
        if list_accounts:
            return sum(i.balance for i in list_accounts)
        return 0


def create_account_number():
    account_number = randint(1_000_000, 9_999_999)
    while account_number in BankAccount.reserved_accounts:
        account_number = randint(1_000_000, 9_999_999)
    return account_number


class BankAccount:
    list_accounts = {}
    reserved_accounts = []

    def __init__(self, master: object, balance: float = 0, credit_limit: float = 0):
        self.master = master
        self.balance = balance
        self.account_number = create_account_number()
        self.credit_limit = credit_limit
        BankAccount.list_accounts.setdefault(self.master, []).append(self)
        BankAccount.reserved_accounts.append(self.account_number)

    def __str__(self):
        return (f'Master of account: {self.master}\n'
            f'\tAccount Number: {self.account_number}\n'
            f'\tBalance: {self.balance}\n'
            f'\tCredit Limit: {self.credit_limit}')

    def __repr__(self):
        return str(self.account_number)

    def show_balance(self):
        print(f'Account Number: {self.account_number}\n\tBalance: {self.balance}')

    def deposits(self, amount):
        self.balance = self.balance + amount
        self.show_balance()

    def withdraw(self, amount):
        if self.balance + self.credit_limit >= amount:
            self.balance = self.balance - amount
            self.show_balance()
        else:
            raise NotEnoughMoney


# Testing
i_am = Person('Volodymyr', 'Mutaf', date(1900, 2, 5))
my_account1 = BankAccount(i_am, balance=50, credit_limit=0)

my_account1.deposits(1_000_000)

my_account2 = BankAccount(i_am, balance=1000, credit_limit=100)
my_account2.deposits(100)
my_account2.withdraw(50)
# my_account2.withdraw(5000)
print(BankAccount.list_accounts)
print(i_am.get_all_accounts())
print(i_am.get_all_money())
