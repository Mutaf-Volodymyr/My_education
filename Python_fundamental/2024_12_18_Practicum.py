import requests
from bs4 import BeautifulSoup
import os


response = requests.get('https://www.flickr.com/explore/')
fotis_list = []
if response.status_code == 200:
    os.makedirs('photos', exist_ok=True)
    soup = BeautifulSoup(response.text, 'html.parser')
    link_foto = soup.find_all('img')
    for link in link_foto:
        link = link.get('src')
        if not link.startswith('http'):
            link = 'https:' + link
        fotis_list.append(link)

else:
    print('Error')

for num, link in enumerate(fotis_list[:2], start=1):
    response = requests.get(link)
    if response.status_code == 200:
        with open(f'photos/{num}.jpg', 'wb') as f:
            f.write(response.content)



