# -*- coding: utf-8 -*-
import requests, bs4
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0'}
print("Привет!!!\nЭто просто программа для тру пикабушников. Введи ник автора: \nПример: test")
AuthorName=input()
UrlPart1="https://pikabu.ru/@"+AuthorName #
PageNumber=1
UrlPart2="?page="
urlall=UrlPart1+UrlPart2+str(PageNumber)
r = requests.get(urlall, headers = header) # передаем заголовок запроса, чтобы нас не распознали как бота
b=bs4.BeautifulSoup(r.text, "html.parser")
title = b.select('a.story__title-link.story__title-link_visited') # получаем названии истории
title_text = title[0].getText()
print(title_text)
