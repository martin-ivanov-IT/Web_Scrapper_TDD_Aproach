from bs4 import BeautifulSoup
from module.data_formatter import DataFormatter
from module.Article import Article
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

    @classmethod
    def get_all_articles_urls(cls, neededURLS):
        articlesUrls = []
        page = 1
        while len(articlesUrls) < neededURLS:
            web_scrapper = WebScrapper(f"https://blog.bozho.net/page/{page}")
            web_scrapper.makeSoup()
            articlesNeeded = neededURLS - len(articlesUrls)
            lis = web_scrapper.get_articles_urls("a", "more-link", articlesNeeded)
            articlesUrls.extend(lis)
            page += 1
        return articlesUrls

    @classmethod
    def get_all_articles(cls, articlesUrls):
        articlesList = []
        for article in articlesUrls:
            currWS = WebScrapper(article)
            currWS.makeSoup()
            currWS.delete_elements_by_class("div", "swp_social_panel")
            title = currWS.get_title("h1")
            content = currWS.get_content("div", "entry-content clearfix")
            date = currWS.get_date("time", "entry-date published updated")
            cms = currWS.get_comments()
            currArticle = Article(title, date, content, cms)
            currArticle.set_most_used_words()
            currArticle.set_content_to_first_three_paragraphs()

            articlesList.append(currArticle)
        return articlesList
