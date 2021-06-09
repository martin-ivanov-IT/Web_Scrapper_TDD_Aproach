import argparse
import module  # This will not link correctly if you use from imports
from module.web_scraper import WebScrapper
import csv
import codecs


FILENAME = "test.csv"
ENCODING = 'utf-16'

with codecs.open(FILENAME, "w", ENCODING) as fp:
    web_scrapper = WebScrapper("https://blog.bozho.net/")
    writer = csv.writer(fp)
    web_scrapper.makeSoup()
    articlesUrls = web_scrapper.get_articles_urls('a', 'more-link', 3)
    for article in articlesUrls:
        currWS = WebScrapper(article)
        currWS.makeSoup()
        title = currWS.get_title('h1')
        content = currWS.get_content('div', 'entry-content clearfix')
        date = currWS.get_date('time', 'entry-date published updated')
        print(title.upper())
        print(article)
        print(content)
        print(date)
        writer.writerow([title, date, content])
fp.close()

print("-----------")
with codecs.open(FILENAME, "r", ENCODING) as fp:
    csv_reader = csv.reader(fp)
    for row in csv_reader:
        print(row)