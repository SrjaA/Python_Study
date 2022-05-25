import random
import time
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import os
import pyexcel

HOST = 'https://bamper.by/'


def get_html(url):
    '''Site Request Function'''
    with open('./files/desktop_user_agent.txt', 'r', newline='', encoding='utf-8') as base:
        user_agent_base = base.readlines()
        user_agent_list = [i.strip() for i in user_agent_base]
        user_agent = random.choice(user_agent_list)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*; \
        q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": user_agent,
    }
    request = requests.get(url, headers=headers)
    return request


def get_content(html, path_2):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item-list')
    with open(path_2, 'r', newline='', encoding='utf-8') as file:
        reader = tuple(csv.reader(file, delimiter=';', quotechar='|'))
    article_base = [i[2] for i in reader]
    page_cards = []
    for item in items:
        item.b.decompose()
        if item.find('span', class_='date').text.strip() in article_base:
            continue
        else:
            try:
                price = int(item.find('div', class_='mobile-currency').find('span').get_text()[1:-1])
            except AttributeError:
                price = 0
            page_cards.append(
                {
                    'title': item.find('h5', class_='add-title').find('a').text.replace('  к ', '').rstrip(),
                    'link-product': HOST + item.find('h5', class_='add-title').find('a').get('href'),
                    'article': item.find('span', class_='date').text.strip(),
                    'price': price,
                    'city': item.find('span', class_='city').get_text().strip()
                }
            )

    return page_cards


def save_doc(items, path_1, path_2):
    with open(path_1, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # writer.writerow(['Car', 'Link', 'Article', 'Price', 'Town'])
        for item in items:
            writer.writerow([item['title'], item['link-product'], item['article'], item['price'], item['city']])
    with open(path_2, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for item in items:
            writer.writerow([item['title'], item['link-product'], item['article'], item['price'], item['city']])


def parser(url, path_1, path_2, pagenation_quantity=2):
    html = get_html(url)
    if html.status_code == 200:
        time_start = time.time()
        print(f'Parsing start on {time.asctime()}')
        cards = []
        for page in range(1, pagenation_quantity + 1):
            print(f'Parsing page: {page}')
            html = get_html(url=f'{url}?PAGEN_1={page}')
            print(html.url)
            cards.extend(get_content(html.text, path_2))
            for i in tqdm(range(random.randint(5, 10)), desc='Pause of request'):
                time.sleep(1)
        save_doc(cards, path_1, path_2)
        print(f'Parsing end {(time.time() - time_start) // 60:.0f} min, {(time.time() - time_start) % 60:.0f} s')

    else:
        print(f'Сайт отвечаэ не так... {html.status_code}')


def main():
    # run parsing process
    parser('https://bamper.by/zchbu/zapchast_avtonomnyy-otopitel/', './files/heater_last.csv',
           './files/heater_old.csv', int(input('Specify the number of pages to parse: ')))

    # convert csv to xlsx and open xlsx-file in OS
    pyexcel.get_sheet(file_name='./files/heater_last.csv', delimiter=";").save_as('./files/today_parsing.xlsx')
    os.startfile(r'G:\Мой диск\Python_Study\parser\files\today_parsing.xlsx')


if __name__ == '__main__':
    main()

# parser('https://bamper.by/zchbu/zapchast_pult-upravleniya-avtonomnym-otopitelem/', './files/timer_last.csv',
#            './files/timer_old.csv')
