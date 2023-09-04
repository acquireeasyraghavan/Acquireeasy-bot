from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless=new')

from selenium.webdriver.common.by import By
driver = webdriver.Chrome( options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get('https://scrapingclub.com')
exercise1_card = driver.find_element(By.CLASS_NAME, 'w-full.rounded.border')