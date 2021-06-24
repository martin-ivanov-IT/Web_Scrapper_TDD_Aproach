import json

FILENAME = "data.json"
ENCODING = 'utf-16'


def get_data():
    """
    gets all data as Python object form json file
    @rtype: list
    """
    with open(FILENAME, encoding=ENCODING, errors='ignore') as json_data:
        data = json.load(json_data, strict=False)
        json_data.close()
        return data


def get_article_by_id(article_id):
    """
    @param article_id:
    @type article_id:
    @return:
    @rtype: Article
    """
    data = get_data()
    for article in data:
        if article["id"] == article_id:
            return article
    return None


def get_article_content_by_id(article_id):
    """

    @param article_id:
    @type article_id:
    @return:
    @rtype: str
    """
    data = get_data()
    for article in data:
        if article["id"] == article_id:
            return article["content"]
    return None


def get_most_used_words_by_id(article_id):
    """

    @param article_id:
    @type article_id:
    @return:
    @rtype: dict
    """
    data = get_data()
    for article in data:
        if article["id"] == article_id:
            return article["most_used_words"]
    return None
