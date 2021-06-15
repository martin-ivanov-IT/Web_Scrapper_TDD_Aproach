import pytest
from module.web_scraper import WebScrapper
from bs4 import BeautifulSoup
from module.Article import Article
import collections


@pytest.fixture()
def webScrapperDemo():
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeSoup()
    return ws


@pytest.fixture()
def webFirstArticle():
    ws = WebScrapper("https://blog.bozho.net/blog/3733")
    ws.makeSoup()
    ws.delete_elements_by_class("div", 'swp_social_panel')
    return ws


@pytest.fixture()
def localFirstArticleSoup():
    with open("H:/Python/PyTest/Demo/test/unit_tests/test_files/firstArticleHTML.html", encoding="utf-8") as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents, "lxml")
        for div in soup.find_all("div", class_="swp_social_panel"):
            div.decompose()
        return soup


@pytest.fixture()
def urls_list():
    urlsList = ["https://blog.bozho.net/blog/3733", "https://blog.bozho.net/blog/3728",
                "https://blog.bozho.net/blog/3722"]
    return urlsList


@pytest.fixture(webFirstArticle)
def article_obj():
    title = webFirstArticle.get_title("h1")
    content = webFirstArticle.get_content("div", "entry-content clearfix")
    date = webFirstArticle.get_date("time", "entry-date published updated")
    cms = webFirstArticle.get_comments()
    article = Article(title, date, content, cms)
    return article


def test_WebScrapperClass(webScrapperDemo):
    assert isinstance(webScrapperDemo, WebScrapper)


def test_make_soup(webScrapperDemo):
    assert isinstance(webScrapperDemo.soup, BeautifulSoup)


def test_main_Page_soup(webScrapperDemo):
    ws = WebScrapper("https://blog.bozho.net/")
    ws.makeSoup()
    assert webScrapperDemo.soup.text == ws.soup.text


def test_get_articles_urls(urls_list, webScrapperDemo):
    articlesUrls = webScrapperDemo.get_articles_urls(atr='a', classAtr='more-link', articlesNeeded=3)
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
