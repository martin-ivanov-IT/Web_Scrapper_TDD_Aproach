import csv

class Writer:
    def __init__(self, fp):
        self.writer = csv.writer(fp)

    def writeRowToFile(self, title, date, content):
        self.writer.writerow([title, date, content])
