from django import forms
from .models import news_post
from django.forms import ModelForm, TextInput, Textarea, DateInput

class news_postForm(forms.ModelForm):
    class Meta:
        model = news_post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Новость'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder':'Дата публикации'}),
        }

