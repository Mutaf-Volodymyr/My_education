# Сгенерировать все пароли, состоящие из 4 символов чтобы среди них была хотя бы одна
# большая латинская буква, одна маленькая, одна цифра и никаких иных типов символов.
# При этом запрещено, чтобы символ повторялся в пароле или две соседние по алфавиту буквы
# стояли рядом. Записать полученные пароли в файл.

from itertools import combinations
from string import ascii_uppercase, ascii_lowercase, digits


def is_valid_password(pas):
    if pas == pas.upper() or pas == pas.lower():
        return False
    if not any(i.isdigit() for i in pas):
        return False
    for el1, el2 in zip(pas[:-1], pas[1:]):
        if el1.isalpha() and el2.isalpha() and abs(ord(el1) - ord(el2)) < 2:
            return False
    return True

with open('passwords.txt', 'w') as out:
    res1 = combinations(ascii_uppercase + ascii_lowercase + digits, r=4)
    res2= map(''.join, res1)
    res3 = filter(is_valid_password, res2)
    print(*res3, file=out, sep='\n')



