import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv() 
r = requests.get("https://acquire.com/")
print(r)


soup = BeautifulSoup(r.content, 'html.parser')
var = soup.prettify()
print(type(var))
with open('output.txt', 'w',encoding='utf-8') as file:
    file.write(var)