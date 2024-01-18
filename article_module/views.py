from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from article_module.models import Article, ArticleCategory
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali


# Create your views here.
class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__urlTitle__iexact=category_name)
        return query


def ArticleCategories_Component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)

    context = {
        'main_categories': article_main_categories
    }
    return render(request, 'article_module/components/article_categories_component.html', context)
