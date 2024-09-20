from django.shortcuts import render, get_object_or_404, redirect
from .forms import news_postForm
from .models import news_post


def home(request):
    news = news_post.objects.all()
    return render(request, "news/news.html", {"news": news})

def news_detail(request, id):
    news = get_object_or_404(news_post, id=id)
    return render(request, 'news/news_detail.html', {'news': news})

def create_news(request):
    error = ""
    if request.method == 'POST':
        form = news_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма заполнена неверно"
    form = news_postForm()
    return render(request, 'news/add_news.html', {'form': form, 'error': error})
