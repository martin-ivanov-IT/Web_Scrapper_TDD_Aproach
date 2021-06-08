import requests
from html import unescape
from bs4 import BeautifulSoup



class WebScrapper:
    def __init__(self, url):
        self.url = url
        self.dataDictionary = None
        self.soup = None

    def makeDataDictionary(self):
        html = requests.get(self.url)
        if html.status_code == 404:
            return None

        text = html.text
        soup = BeautifulSoup(text, "lxml")
        self.dataDictionary = {"html": html, "text": text, "soup": soup}
        self.soup = soup

    def get_articles_urls(self, atr, classAtr, articlesNeeded):
        return self.dataDictionary['soup'].find_all(atr, class_= classAtr)[:articlesNeeded]

    def get_content(self, atr, classAtr):
        text = self.dataDictionary.soup.find(atr, class_=classAtr).get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    def get_title(self, atr):
        title = self.dataDictionary.soup.find(atr).text
        return title

    def get_date(self, atr, classAtr):
        date = self.dataDictionary.soup.find(atr, class_=classAtr).text
        return date
