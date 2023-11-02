import json
from model import Author, Quote
import os

# Підключення до бази даних MongoDB
from conn import connect_to_mongodb
connection = connect_to_mongodb()




with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)

# Збереження даних у колекції "authors"
for author_info in authors_data:
    # Перевірка наявності ключів та їх використання
    # Порожній рядок, якщо ключ відсутній
    fullname = author_info.get('fullname', '') 
    born_date = author_info.get('born_date', '') 
    born_location = author_info.get('born_location', '') 
    description = author_info.get('description', '')  

    # Створення об'єкта authors з врахуванням відсутніх ключів
    author = Author(
        fullname=fullname,
        born_date=born_date,
        born_location=born_location,
        description=description
    )
    author.save()




current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'quotes.json')

with open(file_path, 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

    # Збереження даних у колекції "quotes"
    for quote_info in quotes_data:
        author_name = quote_info.get('author', '')  
        # значення ключа 'author', або порожнього рядка

        # Знаходження або створення об'єкта автора
        author = Author.objects(fullname=author_name).first()
        if not author:
            author = Author(fullname=author_name)
            author.save()

        # Перевірка наявності ключа 'tags'
        if 'tags' in quote_info:
            tags = quote_info['tags']
        else:
            tags = []  # порожній список, якщо ключ 'tags' відсутній


        # add об'єкта цитати за відсутності ключів 'author' та 'tags'
        quote_text = quote_info.get('quote', '')  
        # значення ключа 'quote', або порожнього рядка
        
        quote = Quote(
            tags=tags,
            author=author,  # Посилання на об'єкт автора
            quote=quote_text
        )
        quote.save()
