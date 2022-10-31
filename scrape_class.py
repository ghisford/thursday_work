# php -S localhost:5000   how to connect to the localhost using php

from turtle import title
from bs4 import BeautifulSoup

htmle = '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Document</title>
            </head>
            <body>
                <h1>Web Scraping</h1>
                <p>Web scraping is a technique to automatically access and extract large amounts of information from a website, which can save a huge amount of time and effort.</p>
                <p>Web scraping can be done manually through a web browser. However, this process is both time-consuming and error-prone. Fortunately, there are several web scraping tools that can help you automate the process.</p>
                <p>Web scraping tools can be used to extract data from websites and save it to a local file or database in a structured format. This data can then be used for a variety of purposes, including data mining, data processing, data cleansing, and data analysis.</p>
                <p>Web scraping tools can be used to extract data from websites and save it to a local file or database in a structured format. This data can then be used for a variety of purposes, including data mining, data processing, data cleansing, and data analysis.</p>
            </body>
            </html>'''

soop = BeautifulSoup(htmle,'html.parser')
# print(soop.prettify())
title = soop.title.text
sentence = soop.p.string

print(f"The title is {title} and that's {sentence} baby ")

paragraph_list = soop.find_all('p')

for index,paragraph in enumerate(paragraph_list):
    print(f"paragraph {index + 1} \n\n {paragraph.text}\n")