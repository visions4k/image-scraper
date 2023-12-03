import requests
from bs4 import BeautifulSoup
from config import *

class ImageScraper:
    def __init__(self):
        self.keywords = keywords

    def getUrls(self, key):
        url = f"https://www.google.com/search?tbm=isch&q={key}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return [img['src'] for img in img_tags if 'src' in img.attrs and img['src'].startswith('http')]

    def scrapeImages(self):
        count = 0
        with open("output/images.txt", 'w') as f:
            for key in self.keywords:
                image_urls = self.getUrls(key)
                for url in image_urls:
                    f.write(url + '\n')
                    count += 1
        print(f"\033[92mSuccessfully scraped {count} pictures.\033[0m")
