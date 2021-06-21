from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path('article/<int:article_id>/', views.article_by_id),
    path('article/demo/<int:demo_id>/', views.article_demo),
    path('article/comments/<int:article_id>/', views.comments_by_article_id),
    path('article/content/<int:article_id>/', views.content_by_article_id),
]
