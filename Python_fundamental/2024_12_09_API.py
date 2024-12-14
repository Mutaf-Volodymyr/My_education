
from re import findall

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter







# https://catfact.ninja/fact
# response = requests.get('https://catfact.ninja/fact')
# if response.status_code == 200:
#     fact = response.json()['fact']
#     print(fact)
#     res = re.search(r'[^\w .,]', fact)
#     if res is not None:
#         print(False)
#     else: print(True)



# 11. Напишите программу, которая заменяет пробелы подчеркиваниями и обратно.
# response = requests.get('https://catfact.ninja/fact')
# if response.status_code == 200:
#     fact = response.json()['fact']
#     fact = re.sub(r' ', '_', fact)
#     print(fact)
#     fact = re.sub(r'_', ' ', fact)
#     print(fact)


# 12. Частью URL часто является дата в формате 2016/09/02. Например,
# https://www.somesite.com/news/2024/01/22/article.html. Найдите все даты в URL такого вида.
# Вывод может выглядеть так [('2024', '01', '22')].

# text = 'https://www.somesite.com/news/2024/01/22/article.html'
# pattern = r'\d{4}/\d{2}/\d{2}'
# res = re.findall(pattern, text)
# print(res)

# 13. Напишите программу, которая конвертирует дату в формате yyyy-mm-dd в формат
# dd-mm-yyyy.

# text = 'https://www.somesite.com/news/2024/01/22/article.html'
# pattern = r'\d{4}/\d{2}/\d{2}'
# res = re.findall(pattern, text)
# print(res)

from bs4 import BeautifulSoup
import requests
import re


response = requests.get('https://wise.com/ru/currency-converter/usd-to-eur-rate').text
soup = BeautifulSoup(response, 'html.parser')
links = soup.find_all(class_='d-inline-block')
res = ''
for link in links:
    if 'EUR' in link:
        res = link



print(res)