import requests
from requests.exceptions import HTTPError
import csv


class DataFormatter:
    def __init__(self, url):
        self.html = None
        self.url = url

    # fetches the html using requests library and sets the html field to it
    def fetchHtml(self):
        try:
            html = requests.get(self.url)
            html.raise_for_status()
            self.html = html
            return html.text
        except HTTPError:
            print("could not load url")
            raise HTTPError
