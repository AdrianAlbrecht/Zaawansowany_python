import requests
from bs4 import BeautifulSoup
import random

def get_random_wikipedia_article():
    url = "https://pl.wikipedia.org/wiki/Special:Random"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', {'class': 'firstHeading'}).text
        article_text = ""
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            article_text += paragraph.get_text() + '\n'
        return title, article_text
    else:
        print("Nie można pobrać artykułu z Wikipedii.")
        return None, None

def save_article_to_file(title, article_text):
    if title and article_text:
        filename = f"./Lab_02/{title}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(article_text)
        print(f"Artykuł '{title}' został zapisany w pliku '{filename}'.")


title, article_text = get_random_wikipedia_article()
save_article_to_file(title, article_text)
