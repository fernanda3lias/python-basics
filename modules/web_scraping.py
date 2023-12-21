# + Web Scraping with Python using requests and bs4 BeautifulSoup
# - Web Scraping is the act of "scraping the web" for information in an
# automated way, using a particular programming language, for later use.
# - The requests module can load data from the Internet into your code.
# Meanwhile, bs4.BeautifulSoup is responsible for parsing HTML data into
# Python objects, making the developer's life easier.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.otaviomiranda.com.br/'
response = requests.get(url)
parsed_html = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

# if parsed_html.title is not None:
#     print(parsed_html.title)

about_heading = parsed_html.select_one('#about')

if about_heading is not None:
    about_parent = about_heading.parent
    
    for p in about_parent.select('p'):
        print(re.sub(r'\s{1,}', ' ', p.text))

# IMPORTANT
# To read -> https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/