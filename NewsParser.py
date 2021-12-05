import json

import requests
from bs4 import BeautifulSoup


def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    url = "https://www.securitylab.ru/news/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    articles_cards1 = soup.find("div", class_="row")
    articles_cards = articles_cards1.find_all("a", class_="article-card inline-card")
    # print(articles_cards)

    news_dict = {}
    for article in articles_cards:
        article_title = article.find("h2", class_="article-card-title").text.strip()
        try:
            article_desc = article.find("p").text.strip()
        except:
            article_desc = "Нет описания"
        article_url = f'https://www.securitylab.ru{article.get("href")}'
        article_date_time = article.find("time").text.strip()
        article_id = article.get("id")

        news_dict[article_id] = {
            "article_date_time": article_date_time,
            "article_title": article_title,
            "article_url": article_url,
            "article_desc": article_desc
        }
    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=True)

        # print(f"{article_title} | {article_url} | {article_date_time} | {article_id}")

    # print(len(articles_cards))


def check_news_update():
    with open("news_dict.json") as file:
        news_dict = json.load(file)

        fresh_news = {}

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }
        url = "https://www.securitylab.ru/news/"
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        articles_cards1 = soup.find("div", class_="row")
        articles_cards = articles_cards1.find_all("a", class_="article-card inline-card")


        for article in articles_cards:
            article_url = f'https://www.securitylab.ru{article.get("href")}'
            article_id = article.get("id")
            if article_id in news_dict:
                continue
            else:
                article_title = article.find("h2", class_="article-card-title").text.strip()
                try:
                    article_desc = article.find("p").text.strip()
                except:
                    article_desc = "Нет описания"
                article_date_time = article.find("time").text.strip()


                news_dict[article_id] = {
                    "article_date_time": article_date_time,
                    "article_title": article_title,
                    "article_url": article_url,
                    "article_desc": article_desc
                }
                fresh_news[article_id] = {
                    "article_date_time": article_date_time,
                    "article_title": article_title,
                    "article_url": article_url,
                    "article_desc": article_desc
                }
    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=True)
    return fresh_news


def main():
    get_first_news()

    # print(check_news_update())



if __name__ == '__main__':
    main()
