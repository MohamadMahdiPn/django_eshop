from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Product as prModel
from .models import ProductCategory as prCategory
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.
class ProductListView(ListView):
    template_name = 'product/productList.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     products = prModel.objects.all().order_by('price')
    #     context['products'] = products
    #
    #     return context
    model = prModel
    context_object_name = 'products'

    def get_queryset(self):
        baseQuery = super().get_queryset()
        data = baseQuery.filter(isActive=True)
        return data

class ProductDetailsView(TemplateView):
    template_name = 'product/ProductDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs['slug']
        productItem = get_object_or_404(prModel, slug=slug)
        context['product'] = productItem

        return context


# def productList(request):
#     products = prModel.objects.all().order_by('price')
#     numberOfProducts = products.count()
#     return render(request, 'product/productList.html', {
#         'products': products,
#         'totalNumberOfProducts': numberOfProducts,
#         # 'averageRatings': averageRatings
#
#     })


def productDetail(request, slug):
    # try:
    #    productItem = prModel.objects.get(id=productId)
    # except:
    #     raise Http404()

    productItem = get_object_or_404(prModel, slug=slug)

    return render(request, 'product/ProductDetail.html', {
        'product': productItem
    })
