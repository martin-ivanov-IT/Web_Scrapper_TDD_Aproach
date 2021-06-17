from bs4 import BeautifulSoup
from module.data_formatter import DataFormatter
from module.Article import Article
import collections


class WebScrapper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    # inits soup with the html from data formatter instance and sets the soup field with the fetched soup
    def makeSoup(self):
        df = DataFormatter(self.url)
        html = df.fetchHtml()
        soup = BeautifulSoup(html, "lxml")
        self.soup = soup

    # get the urls from the loaded page in the soup ant return them in a list
    def get_articles_urls_from_page(self, tag, className, articlesNeeded):
        lis = self.soup.find_all(tag, class_=className)[:articlesNeeded]
        urls = [el["href"] for el in lis]
        return urls

    def get_content(self, tag, className):
        text = self.soup.find(tag, class_=className).get_text()
        return text

    def get_title(self, tag):
        title = self.soup.find(tag).text
        return title

    def get_date(self, tag, className):
        date = self.soup.find(tag, class_=className).text
        return date

    # return dictionary with all comments key(author) value(comment)
    def get_comments(self):
        cms = self.soup.find_all("article", class_="comment-body")
        dic = {}
        for el in cms:
            author_name = el.find("b", class_="fn").text
            content = el.find("div", class_="comment-content").text
            dic[author_name] = content

        return dic

    # deletes all elements from the soup with given tag and className
    def delete_elements_by_class(self, tag, className):
        for div in self.soup.find_all(tag, class_=className):
            div.decompose()

    # returns list of urls iterating through the pages until needed count of urls
    @classmethod
    def get_all_articles_urls(cls, neededURLS):
        articlesUrls = []
        page = 1
        while len(articlesUrls) < neededURLS:
            web_scrapper = WebScrapper(f"https://blog.bozho.net/page/{page}")
            web_scrapper.makeSoup()
            articlesNeeded = neededURLS - len(articlesUrls)
            lis = web_scrapper.get_articles_urls_from_page("a", "more-link", articlesNeeded)
            articlesUrls.extend(lis)
            page += 1
        return articlesUrls

    # returns Article list filled with the whole articles content
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

            # if this line is moved after the set_content_to_first_three_paragraphs() call
            # the search will be only on the first three paragraphs
            currArticle.set_most_used_words()
            currArticle.set_content_to_first_three_paragraphs()

            articlesList.append(currArticle)
        return articlesList
