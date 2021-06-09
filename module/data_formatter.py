import requests
import csv


class DataFormatter:
    def __init__(self, url):
        self.writer = None
        self.html = None
        self.url = url

    def fetchHtml(self):
        html = requests.get(self.url)
        if html.status_code == 404:
            return None
        self.html = html
        return html.text

    def writeRowToCSV(self, writer, title, date, content):
        writer.writerow([title, date, content])

    def initCSVWriter(self, fp):
        writer = csv.writer(fp)
        self.writer = writer
        return writer
