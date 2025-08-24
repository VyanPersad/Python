from bs4 import BeautifulSoup
import os
import functions
import requests

def main_scraper(url, dir_path):
    functions.create_dir(dir_path)
    src_code = requests.get(url)
    src_text = src_code.text
    soup = BeautifulSoup(src_text,"html.parser")
    ul_elements = soup.find_all("ul", {"class": "css-1he9hsx"})

    for ul in ul_elements:
        text = ul.get_text(separator="\n", strip=True)
        print(text)

def img_scraper(url, dir_path):
    functions.create_dir(dir_path)
    src_code = requests.get(url)
    src_text = src_code.text
    soup = BeautifulSoup(src_text,"html.parser")
    img_elements = soup.find("img", {"class": "thumbnail-item MuiBox-root css-uwwqev"})

    img_url = img_elements.get('src')
    print(img_url)

url = 'https://www.lg.com/us/tvs/lg-55ua7500zua-4k-uhd-tv'
dir_path = "test"

img_scraper(url, dir_path)

