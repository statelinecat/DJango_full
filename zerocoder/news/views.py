from django.shortcuts import render
from .models import news_post

def home(request):
    news = news_post.objects.all()
    return render(request, "news/news.html", {"news": news})
