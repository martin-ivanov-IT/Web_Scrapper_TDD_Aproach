from bs4 import BeautifulSoup
from scrapper.modules.data_formatter import DataFormatter
from scrapper.modules.Article import Article
import collections


class WebScrapper:
    def __init__(self, url):
        """

        @param url:
        @type url:
        """
        self.url = url
        self.soup = None

    def makeSoup(self):
        """
        inits soup with the html from data formatter instance and sets the soup field with the fetched soup
        """
        df = DataFormatter(self.url)
        html = df.fetchHtml()
        soup = BeautifulSoup(html, "lxml")
        self.soup = soup

    def get_articles_urls_from_page(self, tag, className, articlesNeeded):
        """
        get the urls from the loaded page in the soup ant return them in a list
        @param tag:
        @type tag:
        @param className:
        @type className:
        @param articlesNeeded:
        @type articlesNeeded:
        @return:
        @rtype: list
        """
        lis = self.soup.find_all(tag, class_=className)[:articlesNeeded]
        urls = [el["href"] for el in lis]
        return urls

    def get_content(self, tag, className):
        """

        @param tag:
        @type tag:
        @param className:
        @type className:
        @return:
        @rtype: str
        """
        text = self.soup.find(tag, class_=className).get_text()
        return text

    def get_title(self, tag):
        """

        @param tag:
        @type tag:
        @return:
        @rtype: str
        """
        title = self.soup.find(tag).text
        return title

    def get_date(self, tag, className):
        """

        @param tag:
        @type tag:
        @param className:
        @type className:
        @return:
        @rtype: str
        """
        date = self.soup.find(tag, class_=className).text
        return date

    def get_comments(self):
        """
        return dictionary with all comments key(author) value(comment)
        @return:
        @rtype: dict
        """
        cms = self.soup.find_all("article", class_="comment-body")
        dic = {}
        for el in cms:
            author_name = el.find("b", class_="fn").text
            content = el.find("div", class_="comment-content").text
            dic[author_name] = content

        dic = dict(sorted(dic.items(), key=lambda x: x[0].lower()))
        return dic

    def delete_elements_by_class(self, tag, className):
        """
        deletes all elements from the soup with given tag and className
        @param tag:
        @type tag:
        @param className:
        @type className:
        """
        for div in self.soup.find_all(tag, class_=className):
            div.decompose()

    @classmethod
    def get_all_articles_urls(cls, neededURLS):
        """
        returns list of urls iterating through the pages until needed count of urls
        @param neededURLS:
        @type neededURLS:
        @return:
        @rtype:list
        """
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

    @classmethod
    def get_all_articles(cls, articlesUrls):
        """
        returns Article list filled with the whole articles content
        @param articlesUrls:
        @type articlesUrls:
        @return:
        @rtype: list
        """
        articlesList = []
        id = 0
        for article in articlesUrls:
            id += 1
            currWS = WebScrapper(article)
            currWS.makeSoup()
            currWS.delete_elements_by_class("div", "swp_social_panel")
            title = currWS.get_title("h1")
            content = currWS.get_content("div", "entry-content clearfix")
            date = currWS.get_date("time", "entry-date published updated")
            cms = currWS.get_comments()
            currArticle = Article(title, date, content, cms, id)

            # if this line is moved after the set_content_to_first_three_paragraphs() call
            # the search will be only on the first three paragraphs
            currArticle.set_most_used_words()
            currArticle.set_content_to_first_three_paragraphs()

            articlesList.append(currArticle)
        return articlesList
