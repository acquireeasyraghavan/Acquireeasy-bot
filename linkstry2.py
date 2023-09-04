from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://galaxeye.space/')

html = driver.page_source
soup = BeautifulSoup(html)
print(html)