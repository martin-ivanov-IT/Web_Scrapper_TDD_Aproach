import pytest
import requests
from module.web_scraper import WebScrapper
from bs4 import BeautifulSoup
import collections


@pytest.fixture()
def webScrapperDemo():
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeSoup()
    return ws


@pytest.fixture()
def localMainPageSoup():
    with open("mainPageHTML.html", encoding='utf-8') as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents, "html.parser")
        return soup


@pytest.fixture()
def localFirstArticleSoup():
    with open("firstArticleHTML.html", encoding='utf-8') as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents, "html.parser")
        return soup


def test_WebScrapperClass(webScrapperDemo):
    assert isinstance(webScrapperDemo, WebScrapper)


def test_make_soup(webScrapperDemo):
    assert isinstance(webScrapperDemo.soup, BeautifulSoup)


def test_main_Page_soup(localMainPageSoup, webScrapperDemo):
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeSoup()
    assert webScrapperDemo.soup.text == ws.soup.text


def test_get_articles_urls(localMainPageSoup):
    articlesUrlsTest = localMainPageSoup.find_all('a', class_='more-link')[:3]
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeSoup()
    articlesUrls = ws.get_articles_urls(atr='a', classAtr='more-link', articlesNeeded=3)

    assert collections.Counter(articlesUrlsTest) == collections.Counter(articlesUrls)


def test_get_content(localFirstArticleSoup):
    text = localFirstArticleSoup.find('div', class_='post-content').get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    ws = WebScrapper("https://blog.bozho.net/blog/3733")
    ws.makeSoup()
    assert text == ws.get_content('div', 'post-content')


def test_get_title(localFirstArticleSoup):
    title = localFirstArticleSoup.find('h1').text
    ws = WebScrapper("https://blog.bozho.net/blog/3733")
    ws.makeSoup()
    assert title == ws.get_title('h1')


def test_get_date(localFirstArticleSoup):
    date = localFirstArticleSoup.find("time", class_="entry-date published updated").text
    ws = WebScrapper("https://blog.bozho.net/blog/3733")
    ws.makeSoup()
    assert date == ws.get_date("time", "entry-date published updated")
