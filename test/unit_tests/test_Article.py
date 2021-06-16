import pytest
from module.web_scraper import WebScrapper
from module.Article import Article
from bs4 import BeautifulSoup
import collections


def test_set_content_to_first_three_paragraphs(localFirstArticleSoup):
    content = localFirstArticleSoup.find("div", class_="entry-content clearfix").get_text()
    content_modified = content.replace("\n\n", "\n")
    content_modified = content_modified.split('\n')[:4]
    separator = '\n'
    content = separator.join(content_modified)

    article = Article(None, None, content, None)
    article.set_content_to_first_three_paragraphs()
    assert article.content == content


def test_set_most_used_words():
    content = "„hello“ world. world\n spider) spider spider"
    dic = {
        "spider": 3,
        "world": 2,
        "hello": 1,
    }

    article = Article(None, None, content, None)
    article.set_most_used_words()
    assert article.most_used_words == dic
