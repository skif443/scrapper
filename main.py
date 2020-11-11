from time import sleep

import telebot
from bs4 import BeautifulSoup

import requests

bot = telebot.TeleBot("1480349296:AAE-wX8l9Oq4DqEBTdN6DyQAgjJOllteuVA")
page_link ='https://www.technopark.ru/smartfon-apple-iphone-12-pro-128-gb-serebristyy/'

s = requests.Session()
s.headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
}


def get_status():
    page_response = s.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.text, 'html.parser')

    b = soup.find_all('section')
    first_section = b[0]
    c = first_section.find_all('div', class_ = 'product-card__info-right')
    product_card = c[0]
    availability_status = str(product_card.find_all('link')[0])
    if 'PreOrder' in availability_status:
        return 0
    else:
        return 1

while(True):
    status = get_status()
    if (status != 0):
        for i in range(30):
            bot.send_message('136060244', 'Айфон появился!!!')
            sleep(5)
    else:
        print("iPhone is in Pre-order state. Waiting for 300 seconds... ")
    sleep(300)