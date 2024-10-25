from django.db import models
from django.contrib.auth.models import User

class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.TextField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'
        ordering = ['-pub_date']
