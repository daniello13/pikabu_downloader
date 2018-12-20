# -*- coding: utf-8 -*-
import requests, bs4
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0'}
print("Привет!!!\nЭто просто программа для тру пикабушников. Введи ник автора: \nПример: test")
AuthorName=input()
UrlPart1="https://pikabu.ru/@"+AuthorName #
PageNumber=0
UrlPart2="?page="
i=0
tmp=0
title_texts = []
body_texts = []
while tmp!=1: # начало бесконечного цикла на перебор страниц (максимальное количество записей на странице = 10)
    i=0
    PageNumber+=1
    urlall=UrlPart1+UrlPart2+str(PageNumber)
    r = requests.get(urlall, headers = header) # передаем заголовок запроса, чтобы нас не распознали как бота
    b=bs4.BeautifulSoup(r.text, "html.parser")
    title = b.select('a.story__title-link') # получаем названии истории
    story = b.select('div.story__content-inner') #получаем текст истории
    for i in range(len(title)):
        title_texts.append(title[i].getText())
        
    for tmp in range(len(story)):
        body_texts.append(story[tmp].getText())
    if len(title)<10:
        break
# начало записи в БД

