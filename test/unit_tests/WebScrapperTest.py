import pytest
import requests
from module.web_scraper import WebScrapper
from bs4 import BeautifulSoup


@pytest.fixture()
def webScrapperDemo():
    ws = WebScrapper("https://www.travelsmart.bg//")
    ws.makeDataDictionary()
    return ws

@pytest.fixture()
def localMainPageSoup():
    with open("C:\\example.html") as fp:
        soup = BeautifulSoup(fp, 'lxml')
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
