from django.shortcuts import render
from django.views import View

from article_module.models import Article
from django.views.generic.list import ListView

# Create your views here.
class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'