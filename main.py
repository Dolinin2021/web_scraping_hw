import bs4
import requests
from article import article_list


if __name__ == '__main__':

    KEYWORDS = ['дизайн', 'фото', 'web', 'python']

    KEYWORDS_set = set(KEYWORDS)

    response = requests.get('https://habr.com/ru/all/')
    response.raise_for_status()

    text = response.text

    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article', class_='tm-articles-list__item')

    list_of_articles = article_list(articles, KEYWORDS_set)

    for item in list_of_articles:
        print(item)