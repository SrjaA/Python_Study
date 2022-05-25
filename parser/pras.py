import time

import requests
from bs4 import BeautifulSoup
import csv
import random
NOW_CSV = 'heater_last.csv'
OLD_CSV='8heater_old.csv'
HOST = 'https://bamper.by/'
URL = 'https://bamper.by/zchbu/zapchast_avtonomnyy-otopitel/?sort=DATE-DESC'
HEADERS = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

def get_html(url,params=''):
    request = requests.get(url=URL, headers=HEADERS,params=params)
    return request


htmls = get_html(URL)
print(htmls)

def get_content(html):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all('div',class_='item-list')
    cards=[]

    for item in items:
        cards.append(
            {
                'title':item.find('h5',class_='add-title').get_text(strip=True).replace('Автономный отопительк ',''),
                'link-product':HOST + item.find('h5',class_='add-title').find('a').get('href'),
                'article':item.find('span',class_='date').get_text(),
                'price':item.find('div',class_='mobile-currency').find('span').get_text()
            }
        )
    return cards

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer=csv.writer(file,delimiter=';')
        writer.writerow(['Машина','Ссылка','Артикул','Цена'])
        for item in items:
            writer.writerow([item['title'],item['link-product'],item['article'],item['price']])


def parser():
    PAGENATION=int(input('Укажите количество страниц для парсинга: '))
    html=get_html(URL)
    if html.status_code==200:
        cards=[]
        for page in range(1,PAGENATION+1):
            print(f'Парсим страницу: {page}')
            html=get_html(URL,params={'PAGEN_1':page})
            print(html.url)
            cards.extend(get_content(html.text))
            save_doc(cards,NOW_CSV)
            time.sleep((random.randint(5,10)))
    else:
        print('Error')
parser()
# html=get_html(URL)
# print(get_content(html.text))
