import requests
import csv


class DataFormatter:
    def __init__(self, url):
        self.html = None
        self.url = url

    def fetchHtml(self):
        html = requests.get(self.url)
        if html.status_code == 404:
            return None
        self.html = html
        return html.text
