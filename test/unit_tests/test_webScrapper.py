import pytest
from module.web_scraper import WebScrapper
from bs4 import BeautifulSoup
import collections


def test_WebScrapperClass(webScrapperDemo):
    assert isinstance(webScrapperDemo, WebScrapper)


def test_make_soup(webScrapperDemo):
    assert isinstance(webScrapperDemo.soup, BeautifulSoup)


def test_main_Page_soup(webScrapperDemo):
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeSoup()
    assert webScrapperDemo.soup.text == ws.soup.text


def test_get_articles_urls_from_page(urls_list, webScrapperDemo):
    articlesUrls = webScrapperDemo.get_articles_urls_from_page('a', 'more-link', articlesNeeded=3)
    assert collections.Counter(urls_list) == collections.Counter(articlesUrls)


def test_get_content(webFirstArticle, localFirstArticleSoup):
    text = localFirstArticleSoup.find("div", class_="entry-content clearfix").get_text()
    assert text == webFirstArticle.get_content('div', 'entry-content clearfix')


def test_get_comments(webFirstArticle, localFirstArticleSoup):
    cms = localFirstArticleSoup.find_all("article", class_="comment-body")
    dic = {}
    for el in cms:
        author_name = el.find("b", class_="fn").text
        content = el.find("div", class_="comment-content").text
        dic[author_name] = content

    assert dic == webFirstArticle.get_comments()


def test_get_title():
    title = "Какво ще се промени с нови избори?"
    ws = WebScrapper("https://blog.bozho.net/blog/3733")
    ws.makeSoup()
    assert title == ws.get_title('h1')


def test_get_date():
    date = "05.05.2021"
    ws = WebScrapper("https://blog.bozho.net/blog/3733")
    ws.makeSoup()
    assert date == ws.get_date("time", "entry-date published updated")


def test_get_all_articles_urls(article_urls):
    articlesUrls = WebScrapper.get_all_articles_urls(neededURLS=20)
    assert collections.Counter(articlesUrls) == collections.Counter(articlesUrls)


