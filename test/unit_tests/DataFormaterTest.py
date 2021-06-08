import pytest
from module.data_formatter import DataFormatter
import requests


@pytest.fixture()
def dataFormatterDemo():
    df = DataFormatter("https://blog.bozho.net/")
    df.fetchHtml()
    return df


def test_DataFormatterClass(dataFormatterDemo):
    assert isinstance(dataFormatterDemo, DataFormatter)


def test_check_fetchHtml(dataFormatterDemo):
    assert isinstance(dataFormatterDemo.html, requests.Response)
    assert dataFormatterDemo.html


def test_wrong_url():
    url = "http://does_not_exist/"
    ws = DataFormatter(url)

    with pytest.raises(requests.exceptions.ConnectionError):
        ws.fetchHtml()
