import requests
from bs4 import BeautifulSoup
import json

url = 'https://ssr.finanstilsynet.no/Home/Details/NO0010196140'

url = 'https://ssr.finanstilsynet.no/api/v2/instruments/export-json'
response = requests.get(url)


if response.status_code == 200:
    json_data = response.text
   
    target_isin = "NO0010196140"
    for elem in json_data:
        print (elem)