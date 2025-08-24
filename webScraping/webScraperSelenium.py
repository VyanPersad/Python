#Set-up
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

website1 = 'https://www.lg.com/us/tvs/lg-55ua7500zua-4k-uhd-tv'
website2 = 'https://www.standardtt.com/search?q=Samsung&type=article%2Cpage%2Cproduct&options%5Bprefix%5D=last&sort_by=relevance&filter.p.product_type=ELECTRONICS&filter.v.availability=1&filter.p.m.custom.brand=SAMSUNG'
webDriver_path = "C:\webdrivers\msedgedriver.exe"
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get(website2)
time.sleep(30)

prices = driver.find_elements(By.CLASS_NAME,"price__current")
time.sleep(30)
print(len(prices))

for price in prices:
    print(price.text)

