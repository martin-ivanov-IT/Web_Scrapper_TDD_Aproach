import pytest
from module.writer import Writer
import codecs
import json
import collections


def test_WriterClass(writerDemo):
    assert isinstance(writerDemo, Writer)



