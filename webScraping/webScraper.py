from bs4 import BeautifulSoup
import os
import functions
import requests


def main_scraper(url, dir_path):
    functions.create_dir(dir_path)
    src_code = requests.get(url)
    src_text = src_code.text
    soup = BeautifulSoup(src_text,"html.parser")
    print(soup.find_all("div", {"class":"product-card__price sf-price"}))

url = "https://www.pricesmart.com/en-tt/category/Electronics/E10D24?fq=category%3B%22E10D24015%22" 
dir_path = "test"

main_scraper(url, dir_path)
