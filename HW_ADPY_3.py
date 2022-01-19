from datetime import datetime
from urllib import response
import requests
import bs4

HEADERS = {'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
          'Accept-Language': 'ru-RU,ru;q=0.9',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
          'Cache-Control': 'max-age=0',
          'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
          'sec-ch-ua-mobile': '?0'
}

KEYWORDS = {'Дизайн', 'фото', 'Web', 'Python'}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text
#print(text)

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    title = article.find('h2')
    # print(title.text)
    hubs = article.find_all('a', class_="tm-article-snippet__hubs-item-link")
    # hubs = article.find_all('a', class_="tm-article-snippet__title-link")
    article_hubs = set([hub.find('span').text for hub in hubs])
    date_pubs = article.find('time')
    date_publs = date_pubs.attrs['title']
    # print(date_publs)
    # print(article_hubs)
    # print('----')
    if KEYWORDS & article_hubs:
        a_tag = title.find('a')
        href = a_tag.attrs['href']
        url = 'https://habr.com' + href
        print(date_publs, title.text, url)
        print('----')