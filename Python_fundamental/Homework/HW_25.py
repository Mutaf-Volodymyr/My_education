# 1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное
# слово из списка. Аннотируйте типы аргументов и возвращаемого значения функции.

def find_longest_word(text: list[str]) -> str:
    return max(text, key=len)


words = ["apple", "banana", "cherry", "dragonfruit"]
print(find_longest_word(words))
print(*find_longest_word.__annotations__.values())

# 2. Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации
# типов для аргументов и возвращаемых значений функций. Создайте текстовый файл "products.txt",
# в котором каждая строка будет содержать информацию о продукте в формате "название, цена, количество"


import csv


def calculate_total_price(file_in: str, file_out: str, coding: str = "utf-8") -> None:
    with open(file_in, 'r', encoding=coding) as file, open(file_out, 'a', encoding=coding) as out:
        reader = csv.reader(file)
        total_price = 0
        for _, p, k in reader:
            total_price += float(p) * float(k)
        out.write(f"{total_price}\n")


calculate_total_price('HW_25.CSV', 'products.txt')
