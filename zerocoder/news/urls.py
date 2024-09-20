from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='news_home'),
	path('<int:id>/', views.news_detail, name='news_detail'),
	path('create_news', views.create_news, name='add_news'),
]