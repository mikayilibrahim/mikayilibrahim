from django.contrib import admin
from .models import Article


# Register your models here.
#Article


@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","user","create_date"]
    list_display_links= ["title"]
    search_fields = ["title"]
    class Meta:
        model = Article