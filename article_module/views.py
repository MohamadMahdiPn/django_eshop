from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from article_module.models import Article, ArticleCategory, ArticleComment
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali


# Create your views here.
class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__urlTitle__iexact=category_name)
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(is_active=True,
                                                            article_id=article.id,
                                                            parent=None).prefetch_related('articlecomment_set').order_by('-createDate')
        context['comments_count'] = ArticleComment.objects.filter(article_id=article.id).count()
        return context


def ArticleCategories_Component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True, parent_id=None)

    context = {
        'main_categories': article_main_categories
    }
    return render(request, 'article_module/components/article_categories_component.html', context)


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        articleId = request.GET.get('articleId')
        articleComment = request.GET.get('articleComment')
        parentId = request.GET.get('parentId')
        new_article_comment = ArticleComment(article_id=articleId,
                                             text=articleComment,
                                             user_id=request.user.id,
                                             parent_id=parentId, is_active=True)
        new_article_comment.save()
        context={
            'comments':ArticleComment.objects.filter(is_active=True,
                                                            article_id=articleId,
                                                            parent=None).prefetch_related('articlecomment_set').order_by('-createDate'),
            'comments_count': ArticleComment.objects.filter(article_id=articleId).count()

        }
        return render(request, 'article_module/includes/articleCommentsParial.html', context)
    return HttpResponse('response')