from django.contrib import admin
from .models import NewsPost

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'user')
    search_fields = ('title', 'short_description')
    list_filter = ('pub_date', 'user')
    ordering = ('-pub_date',)

admin.site.register(NewsPost, NewsPostAdmin)
