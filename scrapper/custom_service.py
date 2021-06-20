import json

FILENAME = "../data.json"
ENCODING = 'utf-16'


def get_data():
    with open(FILENAME, encoding=ENCODING, errors='ignore') as json_data:
        data = json.load(json_data, strict=False)
        json_data.close()
        return data


def get_article_by_id(article_id):
    with open(FILENAME, encoding=ENCODING, errors='ignore') as json_data:
        data = json.load(json_data, strict=False)
        json_data.close()
        for article in data:
            if article["id"] == article_id:
                return article
        return None
