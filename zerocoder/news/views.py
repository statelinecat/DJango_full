from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewsPostForm
from .models import NewsPost
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    news = NewsPost.objects.all()
    return render(request, "news/news.html", {"news": news})

def news_detail(request, id):
    news = get_object_or_404(NewsPost, id=id)
    return render(request, 'news/news_detail.html', {'news': news})

@login_required
def create_news(request):
    error = ""
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('news_home')
        else:
            error = "Форма заполнена неверно"

    form = NewsPostForm()
    return render(request, 'news/add_news.html', {'form': form, 'error': error})