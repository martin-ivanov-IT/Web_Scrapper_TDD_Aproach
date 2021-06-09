from bs4 import BeautifulSoup
from module.data_formatter import DataFormatter


class WebScrapper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def makeSoup(self):
        df = DataFormatter(self.url)
        html = df.fetchHtml()
        soup = BeautifulSoup(html, "lxml")
        self.soup = soup

    def get_articles_urls(self, atr, classAtr, articlesNeeded):
        return self.soup.find_all(atr, class_=classAtr)[:articlesNeeded]

    def get_content(self, atr, classAtr):
        text = self.soup.find(atr, class_=classAtr).get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    def get_title(self, atr):
        title = self.soup.find(atr).text
        return title

    def get_date(self, atr, classAtr):
        date = self.soup.find(atr, class_=classAtr).text
        return date
