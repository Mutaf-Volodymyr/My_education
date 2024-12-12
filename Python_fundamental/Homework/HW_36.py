# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице.

from bs4 import BeautifulSoup
import requests

# link = input()
link = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html'
response = requests.get(link).text
soup = BeautifulSoup(response, 'html.parser')
links = soup.find_all("a")
for link in links:
    href = link.attrs.get("href")
    if href.startswith("http"):
        print(href)


# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков,
# а затем использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня
# (теги h1, h2, h3 и т.д.) с их текстом.

from bs4 import BeautifulSoup
import requests

# link = input('enter link: ')
# paragraph = input('enter paragraph: ')

link = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html'
titles = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
response = requests.get(link).text
soup = BeautifulSoup(response, 'html.parser')

for title in titles:
    print(f"{title}:")
    for i, h in enumerate(soup.find_all(title), start=1):
        print(f'\t{i}: {h.get_text()}')