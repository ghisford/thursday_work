
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = []
prices = []
ratings = []
driver.get(<a href="/en-us/p/macbook-air-2020-13-inch-m1-8-core-and-7-core-gpu-8gb-ram-ssd-256gb/01c45687-0465-4c8d-93cf-d52b35747910#l=11" data-test="link-title-desktop" title="MacBook Air (2020) 13-inch - Apple M1 8-core and 7-core GPU - 8GB RAM - SSD 256GB" rel="noreferrer noopener" class="line-clamp-2 overflow-hidden no-underline text-black md:leading-6"></a>)
