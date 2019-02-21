import asyncio
import aiohttp
import requests
import time

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']


def sync_parser(url_list):
    started_in = time.time()
    for url in url_list:
        print(f'Starting {url}')
        data = requests.get(url)
        print(f'{url} content length: {len(data.content)} bytes')

    execution_time = time.time() - started_in
    print(f'Total execution time {execution_time}')


async def async_parser(session, url):
    print(f'Starting {url}')
    async with session.get(url) as response:
        content = await response.text()
        print(f'{url} content length: {len(content)} bytes')


async def main(url_list):
    started_in = time.time()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[async_parser(session, url) for url in url_list])

    execution_time = time.time() - started_in
    print(f'Total execution time {execution_time}')


if __name__ == '__main__':
    print('\nSync url parsing runs')
    sync_parser(urls)

    print('\nAsync url parsing runs')
    asyncio.run(main(urls))
