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

EXCHAGE_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


class ExchangeException(Exception):
	pass
	

def get_usd_amount_from_user():
	usd_amount = ''
	while not usd_amount.isdigit():
		usd_amount = input('Введите сумму в долларах: ')
	
	return int(usd_amount)


def get_usd_exchange_rate():
	try:
		responce = request.urlopen(EXCHAGE_URL)
	except (URLError, HTTPError):
		raise ExchangeException('Сервис {0} недоступен'.format(EXCHAGE_URL))

	exchanges_rate = json.loads(responce.read())
	try:
		usd_exchange_rate = exchanges_rate['Valute']['USD']['Value']
	except KeyError:
		raise ExchangeException('Не удалось получить курс USD') 

	return usd_exchange_rate


if __name__ == '__main__':
	usd_amount = get_usd_amount_from_user()
	try:
		usd_exchange_rate = get_usd_exchange_rate()
	except ExchangeException as e:
		exit(e)

	rub_amount = round(usd_amount * usd_exchange_rate, 2)

	print('Текущий курс USD: {0}'.format(usd_exchange_rate))
	print('{0} USD ~ {1} рублей'.format(usd_amount, rub_amount))
