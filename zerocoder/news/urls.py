from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('news/create/', views.create_news, name='add_news'),
]
