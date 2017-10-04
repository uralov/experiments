#!/usr/bin/env python3
"""
Написать консольную программу на Python, которая запрашивает у пользователя
сумму в USD и конвертирует её рубли по текущему курсу ЦБ. 
Программа не должна иметь внешних зависимостей, использовать только
стандартную библиотеку.
"""

import json
from urllib import request
from urllib.error import URLError, HTTPError

EXCHANGE_URL = 'https://query.yahooapis.com/v1/public/yql?q=select+*+from' \
               '+yahoo.finance.xchange+where+pair+=+%22USDRUB%22&format=json' \
               '&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'


class ExchangeException(Exception):
    pass
    

def get_usd_amount_from_user():
    amount = ''
    while not isinstance(amount, float):
        amount = input('Введите сумму в долларах: ')
        try:
            amount = float(amount)
        except ValueError:
            print('Значение должно быть челочисленным или разделённым точкой')
    
    return amount


def get_usd_exchange_rate():
    try:
        response = request.urlopen(EXCHANGE_URL)
    except (URLError, HTTPError):
        raise ExchangeException('Сервис {0} недоступен'.format(EXCHANGE_URL))

    response = response.read().decode(response.headers.get_content_charset())
    exchanges_rate = json.loads(response)
    try:
        exchange_rate = exchanges_rate['query']['results']['rate']['Rate']
    except KeyError:
        raise ExchangeException('Не удалось получить курс USD') 

    return float(exchange_rate)


if __name__ == '__main__':
    usd_amount = get_usd_amount_from_user()
    try:
        usd_exchange_rate = get_usd_exchange_rate()
    except ExchangeException as e:
        exit(e)

    rub_amount = round(usd_amount * usd_exchange_rate, 2)

    print('Текущий курс USD: {0}'.format(usd_exchange_rate))
    print('{0} USD ~ {1} рублей'.format(usd_amount, rub_amount))
