# -*- coding: utf-8 -*-
import requests, bs4, pymysql, re
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
    s = '\"'
    for i in range(len(title)):
        title_texts.append(str(title[i].getText()).replace("\"", re.escape(s)))
       
        
    for tmp in range(len(story)):
        #.append(story[tmp].getText())
        body_texts.append(str(story[tmp].getText()).replace("\"", re.escape(s)))
    if len(title)<10:
        break
# начало работы с  БД
tmp = 0
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',                             
                             db='pikabu',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:

        # SQL 
        lists_sql=[]
        sql = "CREATE TABLE `"+AuthorName+"`(id INT(10) NOT NULL AUTO_INCREMENT Primary key, header TEXT NOT NULL, history LONGTEXT);"
        cursor.execute(sql)
        lists_sql.append(sql)
        #начинаем заносить данные в БД
        for tmp in range(len(title_texts)):
            sql=""
            sql="INSERT INTO `"+AuthorName+"`(header, history) VALUES (\""+title_texts[tmp]+"\",\""+body_texts[tmp]+"\");"
            lists_sql.append(sql)
        finh = "".join(lists_sql)
        cursor.execute(finh)
         
except Exception: 
    #если возникло, таблица уже существует, просто обновляемся
    for tmp in range(len(title_texts)):
            sql=""
            sql="INSERT INTO `"+AuthorName+"`(header, history) VALUES (\""+title_texts[tmp]+"\",\""+body_texts[tmp]+"\");"
            lists_sql.append(sql)
    finh = "".join(lists_sql)
    print (finh)
    cursor.execute(re.escape(finh))
finally:
    # Закрыть соединение (Close connection).      
    connection.close()
