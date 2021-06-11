import argparse
import module  # This will not link correctly if you use from imports
from module.web_scraper import WebScrapper
from module.writer import Writer
import csv
import codecs


def main():  # pragma: no cover
    FILENAME = "data.csv"
    ENCODING = 'utf-16'
    articlesNeeded = 20
    page = 1

    with codecs.open(FILENAME, "w", ENCODING) as fp:
        if fp.closed:
            return 1
        writer = Writer(fp)
        articlesUrls = []
        while len(articlesUrls) < articlesNeeded:
            web_scrapper = WebScrapper(f"https://blog.bozho.net/page/{page}")
            web_scrapper.makeSoup()
            articlesNeeded = articlesNeeded - len(articlesUrls)
            lis = web_scrapper.get_articles_urls("a", "more-link", articlesNeeded)
            articlesUrls.extend(lis)
            page += 1

        for article in articlesUrls:
            currWS = WebScrapper(article)
            currWS.makeSoup()
            currWS.delete_elements_by_class("div", "swp_social_panel")
            title = currWS.get_title("h1")
            content = currWS.get_content("div", "entry-content clearfix")
            date = currWS.get_date("time", "entry-date published updated")
            print(title)
            print(date)
            print(content)
            writer.writeRowToFile(title, date, content)

    fp.close()

    print("-----------")
    with codecs.open(FILENAME, "r", ENCODING) as fp:
        csv_reader = csv.reader(fp)
        for row in csv_reader:
            print(row)
    return 0


if __name__ == "__main__":
    main()
