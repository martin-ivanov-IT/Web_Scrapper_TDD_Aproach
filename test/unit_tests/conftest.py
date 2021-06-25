"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
import pytest
import codecs
from bs4 import BeautifulSoup



# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)
from module.web_scraper import WebScrapper
from module.writer import Writer



@pytest.fixture()
def writerDemo():
    FILENAME = "test/unit_tests/test_files/testWriter.json"
    ENCODING = 'utf-16'
    with codecs.open(FILENAME, "w", ENCODING) as fp:
        writer = Writer(fp)
        return writer


@pytest.fixture()
def localFirstArticleSoup():
    with open("test/unit_tests/test_files/firstArticleHTML.html", encoding="utf-8") as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents, "lxml")
        for div in soup.find_all("div", class_="swp_social_panel"):
            div.decompose()
        return soup


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
def urls_list():
    urlsList = ['https://blog.bozho.net/blog/3743', "https://blog.bozho.net/blog/3733",
                "https://blog.bozho.net/blog/3728"]
    return urlsList


@pytest.fixture()
def article_urls():
    lis = ['https://blog.bozho.net/blog/3743', 'https://blog.bozho.net/blog/3733', 'https://blog.bozho.net/blog/3728', 'https://blog.bozho.net/blog/3722',
           'https://blog.bozho.net/blog/3718', 'https://blog.bozho.net/blog/3714', 'https://blog.bozho.net/blog/3704',
           'https://blog.bozho.net/blog/3691', 'https://blog.bozho.net/blog/3687', 'https://blog.bozho.net/blog/3682',
           'https://blog.bozho.net/blog/3677', 'https://blog.bozho.net/blog/3673', 'https://blog.bozho.net/blog/3669',
           'https://blog.bozho.net/blog/3664', 'https://blog.bozho.net/blog/3659', 'https://blog.bozho.net/blog/3653',
           'https://blog.bozho.net/blog/3647', 'https://blog.bozho.net/blog/3644', 'https://blog.bozho.net/blog/3634',
           'https://blog.bozho.net/blog/3627']
    return lis
