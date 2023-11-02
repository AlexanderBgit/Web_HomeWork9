import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup) #- друк розмітки
# Файл для перевірки розмітки сторінки