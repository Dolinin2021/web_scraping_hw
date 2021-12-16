import re
import bs4
import requests


def processing_of_articles(text, set_name):

    title_value = text.find('a', class_='tm-article-snippet__title-link')

    href = title_value['href']
    url = 'https://habr.com' + href

    pattern = r"[\W]+"

    response = requests.get(url)
    response.raise_for_status()

    body_text = response.text

    soup = bs4.BeautifulSoup(body_text, features='html.parser')
    body_value = soup.text

    correction_body = re.sub(pattern, r" ", body_value)

    splitted_body = correction_body.split()

    body_set = set(splitted_body)

    if set_name & body_set:
        return True
    else:
        return False