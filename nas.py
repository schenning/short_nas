import requests
from bs4 import BeautifulSoup

url = 'https://ssr.finanstilsynet.no/Home/Details/NO0010196140'

url = 'https://ssr.finanstilsynet.no/api/v2/instruments'
response = requests.get(url)


if response.status_code == 200:
    print (response.text)