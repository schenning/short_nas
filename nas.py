import requests
from bs4 import BeautifulSoup

url = 'https://ssr.finanstilsynet.no/Home/Details/NO0010196140'


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')

    
   
    element = soup.find_all('div', {'class': 'container'})
    if element:
        x = list(filter(None, element[4].text.strip().split('\n')))
        
        x = [el.replace('\xa0',' ') for el in x]
        print(x)
       
    else:
        print("Element not found")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)

