import pytest
from module.data_formatter import DataFormatter
import requests
import csv
import codecs
import collections


@pytest.fixture()
def dataFormatterDemo():
    df = DataFormatter("https://blog.bozho.net/")
    df.fetchHtml()

    return df


@pytest.fixture()
def extractedFirstRow():
    with codecs.open("firtArticleExtracted.csv", "r", 'utf-8') as fp:
        csv_reader = csv.reader(fp)
        return next(csv_reader)


def test_DataFormatterClass(dataFormatterDemo):
    assert isinstance(dataFormatterDemo, DataFormatter)


def test_fetchHtml(dataFormatterDemo):
    assert isinstance(dataFormatterDemo.html, requests.Response)
    assert dataFormatterDemo.html


def test_wrong_url():
    url = "http://does_not_exist/"
    ws = DataFormatter(url)

    with pytest.raises(requests.exceptions.ConnectionError):
        ws.fetchHtml()


def test_writeRowToCSV(dataFormatterDemo, extractedFirstRow):
    with codecs.open("testWriter.csv", "w", "utf-8") as fp:
        writer = csv.writer(fp)
        dataFormatterDemo.writeRowToCSV(writer, "test_title", "test_date", "test_content")
    fp.close()
    with codecs.open("testWriter.csv", "r", "utf-8") as fp:
        csv_reader = csv.reader(fp)
        assert collections.Counter(next(csv_reader)) == collections.Counter(extractedFirstRow)
