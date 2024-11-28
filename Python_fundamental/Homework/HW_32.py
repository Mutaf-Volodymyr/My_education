# 1. Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)


class Counter:
    def __init__(self, num=0):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __int__(self):
        return self.num

    def __add__(self, other):
        return self.num + other

    def __radd__(self, other):
        return self.num + other

    def __sub__(self, other):
        return self.num - other

    def __rsub__(self, other):
        return self.num - other


counter = Counter(5)
counter += 3
print(counter)  # Вывод: 8
counter -= 2
print(int(counter))  # Вывод: 6


# 2. Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)



from functools import total_ordering
from datetime import date

@total_ordering
class Email:
    def __init__(self, sender, recipient, title, body, data):
        self.sender = sender
        self.recipient = recipient
        self.title = title
        self.body = body
        self.data = date.fromisoformat(data)

    def __str__(self):
        return f"""From: {self.sender}\nTo: {self.recipient}\nSubject: {self.title}\nBody:\n{self.body}\n"""

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body)

    def __hash__(self):
        return hash(self.body)

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return self.data > other.data



email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")

email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")

email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")


print(email1)  # Вывод:
print(len(email2))  # Вывод: 24
print(hash(email3))  # Вывод: -920444056
print(bool(email1))  # Вывод: True
print(email2 > email3)  # Вывод: True