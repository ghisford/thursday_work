from urllib import response
from numpy import number
import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://unsplash.com/s/photos/uganda"

response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

images = soup.find_all('img',attrs = {'alt':'Post image'})

number = 0

with open('pics.png','wb') as f:
    for image in images:
        image_src = image['src']
        f.write(image_src)
        # urllib.request.urlretrieve(image_src,str(number))
        # number += 1