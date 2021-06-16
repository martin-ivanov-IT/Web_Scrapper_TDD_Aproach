import pytest
from module.web_scraper import WebScrapper
from module.Article import Article
from bs4 import BeautifulSoup
import collections


def test_set_content_to_first_three_paragraphs( localFirstArticleSoup):
    content = localFirstArticleSoup.find("div", class_="entry-content clearfix").get_text()
    content_modified = content.replace("\n\n", "\n")
    content_modified = content_modified .split('\n')[:4]
    separator = '\n'
    content = separator.join(content_modified)

    article = Article(None, None, content, None)
    article.set_content_to_first_three_paragraphs()
    assert article.content == content


def test_set_most_used_words(localFirstArticleSoup):
    content = localFirstArticleSoup.find("div", class_="entry-content clearfix").get_text()
    wordcount = {}
    for word in content.lower().split():
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace(";", "")
        word = word.replace("\n", " ")
        word = word.replace("\n\n", " ")
        word = word.replace("\"", "")
        word = word.replace("„", "")
        word = word.replace("“", "")
        word = word.replace("!", "")
        word = word.replace("?", "")
        word = word.replace(")", "")
        word = word.replace("(", "")
        word = word.replace("*", "")
        if len(word) < 4:
            continue

        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    word_counter = collections.Counter(wordcount)
    most_used_words = dict(word_counter.most_common(3))

    article = Article(None, None, content, None)
    article.set_most_used_words()
    assert article.most_used_words == most_used_words
