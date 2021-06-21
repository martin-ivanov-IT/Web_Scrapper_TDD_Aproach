from django.shortcuts import render
from django.http import HttpResponse
from scrapper import custom_service
from scrapper import main
from django.core.paginator import Paginator

main.main()


# Create your views here.
def index(request):
    with open("../scrapper/data.json", encoding='utf-16', errors='ignore') as json_data:
        articles = custom_service.get_data()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page', 1)
    articles = paginator.page(page)
    return render(request, "main/base.html", {"articles": articles})


def home(response):
    return render(response, "main/home.html", {})


def article_by_id(response, article_id):
    article = custom_service.get_article_by_id(article_id)
    return render(response, "main/article_by_id.html", {"article": article})


def article_demo(response, demo_id):
    return render(response, "main/article_demo.html", {"demo_id": demo_id})


def comments_by_article_id(response, article_id):
    article = custom_service.get_article_by_id(article_id)
    return render(response, "main/comments_by_article_id.html", {"article": article})


def content_by_article_id(response, article_id):
    article_content = custom_service.get_article_content_by_id(article_id)
    return render(response, "main/content_by_article_id.html", {"article_content": article_content})
