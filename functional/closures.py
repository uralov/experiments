# -*- coding: utf-8 -*-
from urllib import urlopen


def get_page(url):
    def get():
        return urlopen(url).read()
    return get

yandex = get_page("http://yandex.ru")
print yandex
print yandex()