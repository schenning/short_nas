import requests
from bs4 import BeautifulSoup

url = 'https://ssr.finanstilsynet.no/Home/Details/NO0010196140'


response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Find and print the text inside a specific HTML element
   
    element = soup.find_all('div', {'class': 'container'})
    if element:
        x = list(filter(None, element[4].text.strip().split('\n')))
        
        x = [el.replace('\xa0',' ') for el in x]
        print(x)
       
    else:
        print("Element not found")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)


position_data = []
current_position = {}
data_list = x
for item in data_list:
    key = 'Position Holder'
    if key not in current_position:
        current_position[key] = item
    else:
        current_position[key] = item
        key = 'Short Position'
    if key not in current_position:
        current_position[key] = item
    else:
        current_position[key] = item
        key = 'Short Percent'
    if key not in current_position:
        current_position[key] = item
    else:
        current_position[key] = item
        key = 'Position Date (dd.mm.yyyy)'
    if key not in current_position:
        current_position[key] = item

# Print the list of dictionaries
for position in position_data:
    print(position)