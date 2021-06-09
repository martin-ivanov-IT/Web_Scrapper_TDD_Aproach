import argparse
import module  # This will not link correctly if you use from imports
from module.web_scraper import WebScrapper
from module.writer import Writer
import csv
import codecs


FILENAME = "test.csv"
ENCODING = 'utf-16'

with codecs.open(FILENAME, "w", ENCODING) as fp:
    web_scrapper = WebScrapper("https://blog.bozho.net/")
    writer = Writer(fp)
    web_scrapper.makeSoup()
    articlesUrls = web_scrapper.get_articles_urls('a', 'more-link', 1)
    for article in articlesUrls:
        currWS = WebScrapper(article)
        currWS.makeSoup()
        currWS.delete_elements_by_class("div", 'swp_social_panel')
        title = currWS.get_title('h1')
        content = currWS.get_content('div', 'entry-content clearfix')
        date = currWS.get_date('time', 'entry-date published updated')
        print(title.upper())
        print(article)
        print(content)
        print(date)
        writer.writeRowToFile(title, date, content)
fp.close()

print("-----------")
with codecs.open(FILENAME, "r", ENCODING) as fp:
    csv_reader = csv.reader(fp)
    for row in csv_reader:
        print(row)