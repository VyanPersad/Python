from bs4 import BeautifulSoup
import functions
import requests

def main_scraper(url, dir_path):
    functions.create_dir(dir_path)
    src_code = requests.get(url)
    src_text = src_code.text
    soup = BeautifulSoup(src_text,"html.parser")
    ul_elements = soup.find_all("div", {"class": "product-card__price sf-price"})

    for ul in ul_elements:
        text = ul.get_text()
        print(text)

def img_scraper(url, dir_path):
    functions.create_dir(dir_path)
    src_code = requests.get(url)
    src_text = src_code.text
    soup = BeautifulSoup(src_text,"html.parser")
    img_elements = soup.find("img", {"class": "thumbnail-item MuiBox-root css-uwwqev"})

    img_url = img_elements.get('src')
    print(img_url)

url = 'https://www.pricesmart.com/en-tt/category/Electronics/E10D24?fq=category%3B%22E10D24015%22'
dir_path = "test"

main_scraper(url, dir_path)

