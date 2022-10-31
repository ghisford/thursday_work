from bs4 import BeautifulSoup
import requests
import json
import re

search_term = input('what product do you want to search for?:')

url =  f"https://www.newegg.ca/p/pl?d={search_term}"

page = requests.get(url).text

doc = BeautifulSoup(page,'html.parser')


print(doc)

page_text = doc.find(class_ = "list-tool-pagination-text").strong
page_text = int(str(page_text))

items_found = {}
for page in range(2,page_text+1):
    url = f"{url}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(doc,'html.parser')
    product_div = doc.find('div',class_ = "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = product_div.find_all(text=re.compile(search_term))