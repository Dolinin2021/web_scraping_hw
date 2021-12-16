import re
from datetime import datetime
from process import processing_of_articles


def article_list(text, set_name):

    res_list = []

    for article in text:

        title_value = article.find('a', class_='tm-article-snippet__title-link')
        title = title_value.text.capitalize()

        time = article.find('time')
        date_value = time['datetime']
        date = datetime.strptime(date_value, "%Y-%m-%dT%H:%M:%S.000Z")

        href = title_value['href']
        url = 'https://habr.com' + href

        pattern = r"[\W]+"

        correction_title = re.sub(pattern, r" ", title)

        splitted_title = correction_title.split()

        title_set = set(splitted_title)

        process_of_article = processing_of_articles(article, set_name)

        result = f"{date} - {title} - {url}"

        if set_name & title_set or process_of_article is True:
            res_list.append(result)

    return res_list