import requests
import csv


class DataFormatter:
    def __init__(self, url):
        self.html = None
        self.url = url

    def fetchHtml(self):
        html = requests.get(self.url)
        self.html = html
        return html.text
