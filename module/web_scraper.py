from bs4 import BeautifulSoup
from module.data_formatter import DataFormatter
from module.Comment import Comment
import collections


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
        lis = self.soup.find_all(atr, class_=classAtr)[:articlesNeeded]
        urls = [el["href"] for el in lis]
        return urls

    def get_content(self, atr, classAtr):
        text = self.soup.find(atr, class_=classAtr).get_text()
        return text

    def get_title(self, atr):
        title = self.soup.find(atr).text
        return title

    def get_date(self, atr, classAtr):
        date = self.soup.find(atr, class_=classAtr).text
        return date

    def get_comments(self):
        cms = self.soup.find_all("article", class_="comment-body")
        dic = {}
        for el in cms:
            author_name = el.find("b", class_="fn").text
            content = el.find("div", class_="comment-content").text
            dic[author_name] = content

        return dic

    def delete_elements_by_class(self, atr, classAtt):
        for div in self.soup.find_all(atr, class_=classAtt):
            div.decompose()



