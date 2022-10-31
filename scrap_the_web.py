# find the url
# inspect the page
# find the info you want to scrape
# write the code
# run the code  and extract the info
# store your info in the format of your choice

# checking for scrappability

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.jiji.com/")
print(r.status_code)


