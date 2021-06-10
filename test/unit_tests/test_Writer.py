import pytest
from module.writer import Writer
import codecs
import csv
import collections

@pytest.fixture()
def writerDemo():
    FILENAME = "H:/Python/PyTest/Demo/test/unit_tests/test_files/testWriter.csv"
    ENCODING = 'utf-16'
    with codecs.open(FILENAME, "w", ENCODING) as fp:
        writer = Writer(fp)
        return writer


@pytest.fixture()
def extractedFirstRow():
    with codecs.open("H:/Python/PyTest/Demo/test/unit_tests/test_files/testRaadFile.csv", "r", 'utf-8') as fp:
        csv_reader = csv.reader(fp)
        return next(csv_reader)


def test_WriterClass(writerDemo):
    assert isinstance(writerDemo, Writer)


def test_writeRowToCSV(extractedFirstRow):
    FILENAME = "H:/Python/PyTest/Demo/test/unit_tests/test_files/testWriter.csv"
    ENCODING = 'utf-16'
    with codecs.open(FILENAME, "w", ENCODING) as fp:
        writer = Writer(fp)
        writer.writeRowToFile("test_title", "test_date", "test_content")
    fp.close()
    with codecs.open("H:/Python/PyTest/Demo/test/unit_tests/test_files/testWriter.csv", "r", "utf-16") as fp:
        csv_reader = csv.reader(fp)
        assert collections.Counter(next(csv_reader)) == collections.Counter(extractedFirstRow)
        fp.close()
