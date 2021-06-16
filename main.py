import argparse
import module  # This will not link correctly if you use from imports
from module.web_scraper import WebScrapper
from module.writer import Writer
from module.Article import Article
from bs4 import BeautifulSoup
import csv
import codecs


def main():  # pragma: no cover
    FILENAME = "data.json"
    ENCODING = 'utf-16'
    articlesNeeded = 20
    page = 1

    with codecs.open(FILENAME, "w+", ENCODING) as fp:
        if fp.closed:
            return 1
        writer = Writer(fp)
        articlesUrls = WebScrapper.get_all_articles_urls(neededURLS=articlesNeeded)
        print(articlesUrls)
        articlesList = WebScrapper.get_all_articles(articlesUrls)
        writer.write(articlesList)

    fp.close()

    print("-----------")
    return 0


if __name__ == "__main__":
    main()
