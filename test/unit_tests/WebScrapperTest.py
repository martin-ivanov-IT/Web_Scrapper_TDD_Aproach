import pytest
import requests
from module.web_scraper import WebScrapper
from bs4 import BeautifulSoup
import collections


@pytest.fixture()
def webScrapperDemo():
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeDataDictionary()
    return ws


@pytest.fixture()
def localMainPageSoup():
    with open("mainPageHTML.html", encoding='utf-8') as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents, "html.parser")
        return soup


def test_WebScrapperClass(webScrapperDemo):
    assert isinstance(webScrapperDemo, WebScrapper)


def test_dataDictionaryContents(webScrapperDemo):
    assert isinstance(webScrapperDemo.dataDictionary, dict)
    assert isinstance(webScrapperDemo.dataDictionary["html"], requests.Response)
    assert isinstance(webScrapperDemo.dataDictionary["text"], str)
    assert isinstance(webScrapperDemo.dataDictionary["soup"], BeautifulSoup)
    assert (set(webScrapperDemo.dataDictionary.keys()) == {"text", "soup", "html"})


def test_wrong_url():
    url = "http://does_not_exist/"
    ws = WebScrapper(url)

    with pytest.raises(requests.exceptions.ConnectionError):
        ws.makeDataDictionary()


def test_main_Page_soup(localMainPageSoup, webScrapperDemo):
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeDataDictionary()
    assert webScrapperDemo.soup.text == ws.soup.text


def test_get_articles_urls(webScrapperDemo, localMainPageSoup):
    articlesUrlsTest = localMainPageSoup.find_all('a', class_='more-link')[:3]
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeDataDictionary()
    articlesUrls = ws.get_articles_urls(atr='a', classAtr='more-link', articlesNeeded=3)

    assert collections.Counter(articlesUrlsTest) == collections.Counter(articlesUrls)
