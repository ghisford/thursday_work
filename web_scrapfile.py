# # second way to scrap the web

# from bs4 import BeautifulSoup
# import os

# #                   join   this directory         to this one  
# html_file = os.path.join(os.path.dirname(__file__),'index.html')
# # ../.. means moving back 2 folders


# with open('index.html','r') as html_file:
#     doc = html_file.read()

# print(doc)

# soup = BeautifulSoup(doc,'html.parser')

# this  = soup.find('i').text
# print(this)
# #  all b tags then the last b tag then the child tag of that last b tag
# _italics = soup.find_all('b')[-1].find('i').text.strip()
# print(_italics)






from bs4 import BeautifulSoup
# you can get the attributes of a tag. ie the contents of that tag
# you can also get a specific tag that fulfils a certain requirement

# sauce  = BeautifulSoup('<p class = " first second third" rel= " anotherOne nextOne" ></p>','lxml')

# print(sauce.p['class'])

# print(sauce.p.attrs)



# we can also get all the text from a html file

with open('alice.html','r') as file:
    soup = BeautifulSoup(file,features="lxml")
print(soup.get_text())


# # we can print all the links by treating each tag content like a dictionary
# for link in soup.find_all('a'):
#     print(f"{link.get('id')}\n{link.get('href')}\n")

# get a link with a specific attribute
for link in soup.find_all('a'):
    if link.get('id') == 'link1':
        print(link.get('href'))