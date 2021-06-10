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


def test_DataFormatterClass(dataFormatterDemo):
    assert isinstance(dataFormatterDemo, DataFormatter)
    assert isinstance(dataFormatterDemo.url, str)


def test_fetchHtml(dataFormatterDemo):
    assert isinstance(dataFormatterDemo.html, requests.Response)


def test_wrong_url():
    url = "http://does_not_exist/"
    ws = DataFormatter(url)

    with pytest.raises(requests.exceptions.ConnectionError):
        ws.fetchHtml()


