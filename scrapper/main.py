from scrapper.modules.web_scraper import WebScrapper
from scrapper.modules.writer import Writer
from scrapper.article_service import get_data
import codecs


def main():  # pragma: no cover

    FILENAME = "data.json"
    ENCODING = 'utf-16'
    articlesNeeded = 20

    with codecs.open(FILENAME, "w+", ENCODING) as fp:
        if fp.closed:
            return 1
        writer = Writer(fp)
        articlesUrls = WebScrapper.get_all_articles_urls(neededURLS=articlesNeeded)
        articlesList = WebScrapper.get_all_articles(articlesUrls)
        writer.write(articlesList)

    fp.close()

    print("-----------")

    return 0


if __name__ == "__main__":
    main()
