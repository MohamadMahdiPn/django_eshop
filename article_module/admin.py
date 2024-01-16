from django.contrib import admin
from . import models
# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'urlTitle', 'is_active', 'parent']
    list_editable = ['is_active', 'parent']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    list_editable = ['is_active']


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)