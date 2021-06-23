from django.shortcuts import render
from scrapper import article_service
from django.core.paginator import Paginator
from scrapper.main import main

main()


def index(request):
    articles = article_service.get_data()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page', 1)
    articles = paginator.page(page)
    return render(request, "main/base.html", {"articles": articles})


def article_by_id(response, article_id):
    article = article_service.get_article_by_id(article_id)
    return render(response, "main/article_by_id.html", {"article": article})


def article_demo(response, demo_id):
    return render(response, "main/article_demo.html", {"demo_id": demo_id})


def comments_by_article_id(response, article_id):
    article = article_service.get_article_by_id(article_id)
    return render(response, "main/comments_by_article_id.html", {"article": article})


def content_by_article_id(response, article_id):
    article_content = article_service.get_article_content_by_id(article_id)
    return render(response, "main/content_by_article_id.html", {"article_content": article_content})


def most_used_words_by_article_id(response, article_id):
    most_used_words = article_service.get_most_used_words_by_id(article_id)
    return render(response, "main/most_used_words_by_article_id.html", {"most_used_words": most_used_words})
