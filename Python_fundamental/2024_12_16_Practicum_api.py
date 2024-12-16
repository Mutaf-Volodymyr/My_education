
import requests

url_api_wether = 'https://api.weatherapi.com/v1/current.json?'
url_dict = {
    'key': 'c63902600c8c47d0892121515241612',
    'q': 'Nuremberg',
    'aqi': 'no'
}


response = requests.get(url_api_wether, url_dict).json()

print(response['current']['temp_c'])


