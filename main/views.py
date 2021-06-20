from django.shortcuts import render
from django.http import HttpResponse
from scrapper import custom_service
from scrapper import main

main.main()


# Create your views here.
def index(response):
    with open("../scrapper/data.json", encoding='utf-16', errors='ignore') as json_data:
        articles = custom_service.get_data()
    return render(response, "main/base.html", {"articles": articles})


def home(response):
    return render(response, "main/home.html", {})


def article_by_id(response, article_id):
    article = custom_service.get_article_by_id(article_id)
    return render(response, "main/article_by_id.html", {"article": article})
