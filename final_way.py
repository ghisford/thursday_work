from traceback import print_tb
import requests
from bs4 import BeautifulSoup
import json

url = 'https://cit-projects-2021.github.io/fake-jobs/'
r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

# print(soup.prettify())
# print (soup.h1.text.strip())

cards = soup.find_all(class_= "column is-half")
# print(len(cards))


# print(job_title.text)
# print(company.text)
# print(location.text.strip())
# print(time_is)
jobs = {}

for index,card in enumerate(cards):

    job_title = card.find('h2',class_ = "title is-5").text
    company = card.find('h3',class_  = 'subtitle is-6 company').text
    location  = card.find('p',class_ = 'location' ).text.strip()
    date = card.find('p',class_ ="is-small has-text-grey").find('time').text

    jobs[index+1] = {'job_title':job_title,'company':company,'location':location,'date':date}

with open('jobs.json','w') as json_file:
    json.dump(jobs,json_file,indent= 2)































# list_tags  = soup.find_all('li')

# for index,item in enumerate(list_tags):
#     print(f"{index+1}. {item.text}")
