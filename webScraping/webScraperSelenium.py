#Set-up
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

website1 = 'https://www.pricesmart.com/en-tt/category/Electronics/E10D24?fq=category%3B%22E10D24015%22'
website2 = 'https://www.standardtt.com/search?type=product%2Cpage%2Carticle&options%5Bprefix%5D=last&q=Samsung'
webDriver_path = "C:\webdrivers\msedgedriver.exe"
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get(website1)
time.sleep(1)

prices = driver.find_elements(By.XPATH,'//*[@id="product-card-485340"]/div[2]/div[2]/div[1]/div[1]/div/div/del')
time.sleep(4)
print(len(prices))
for price in prices:
    print(price.text)
