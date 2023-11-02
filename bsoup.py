import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

base_url = 'https://quotes.toscrape.com'
current_page = 1
max_pages = 5  # Задайте тут бажану кількість сторінок, яку ви хочете обійти

quotes_list = []
authors_list = []

while current_page <= max_pages:
    url = f'{base_url}/page/{current_page}/'
    response = requests.get(url)
    
    if response.status_code != 200:
        logger.warning(f"Не вдалося отримати доступ до сторінки {current_page}")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    for quote, author in zip(quotes, authors):
        quote_text = quote.text.strip()
        author_name = author.text.strip()

        # Додавання цитати до списку цитат
        quotes_list.append({
            "author": author_name,
            "quote": quote_text
        })

        # Додавання автора до списку авторів (якщо він ще не доданий)
        if author_name not in [author["fullname"] for author in authors_list]:
            authors_list.append({"fullname": author_name})

    logger.info(f"Завершено обробку сторінки {current_page}")
    current_page += 1

# Запис списків у JSON-файли
with open('quotes.json', 'w', encoding='utf-8') as quotes_file:
    json.dump(quotes_list, quotes_file, ensure_ascii=False, indent=4)

with open('authors.json', 'w', encoding='utf-8') as authors_file:
    json.dump(authors_list, authors_file, ensure_ascii=False, indent=4)
