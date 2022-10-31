from bs4 import BeautifulSoup
import requests
import re

macbook = input('what macbook brand do you want?')
url = 'https://www.backmarket.com/en-us/search?q=macbook'
pages = requests.get(url).text

doc = BeautifulSoup(pages,'html.parser')

page_text = doc.find(class_="body-2-bold")
print(page_text.prettify())



