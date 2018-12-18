# -*- coding: utf-8 -*-
import requests, bs4
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0'}
print("Привет!!!\nЭто просто программа для тру пикабушников. Введи ник автора: \nПример: test")
AuthorName=input()
UrlPart1="https://pikabu.ru/@"+AuthorName #
PageNumber=2
UrlPart2="?page="
urlall=UrlPart1+UrlPart2+str(PageNumber)
r = requests.get(urlall, headers = header) # передаем заголовок запроса, чтобы нас не распознали как бота
b=bs4.BeautifulSoup(r.text, "html.parser")
title = b.select('a.story__title-link') # получаем названии истории
i=0
title_texts = []
for i in range(len(title)):
    title_texts.append(title[i].getText())
    print(title_texts[i])
