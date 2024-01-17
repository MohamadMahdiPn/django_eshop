from django.contrib import admin
from django.http import HttpRequest

from . import models
from .models import Article


# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'urlTitle', 'is_active', 'parent']
    list_editable = ['is_active', 'parent']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)