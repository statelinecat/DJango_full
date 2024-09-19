from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Страница "О нас"
    path('about/', views.about, name='about'),
    # Страница "Наши услуги"
    path('services/', views.services, name='services'),
    # Страница "Контакты"
    path('contact/', views.contact, name='contact'),
]