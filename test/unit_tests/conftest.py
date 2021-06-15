"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
import pytest
from bs4 import BeautifulSoup


# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

@pytest.fixture()
def localFirstArticleSoup():
    with open("H:/Python/PyTest/Demo/test/unit_tests/test_files/firstArticleHTML.html", encoding="utf-8") as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents, "lxml")
        for div in soup.find_all("div", class_="swp_social_panel"):
            div.decompose()
        return soup




