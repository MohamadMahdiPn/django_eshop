from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView

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
    ordering = ['-price']
    paginate_by = 1

    def get_queryset(self):
        baseQuery = super().get_queryset()
        data = baseQuery.filter(isActive=True)
        return data


class ProductDetailsView(DetailView):
    template_name = 'product/ProductDetail.html'
    model = prModel

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     slug = kwargs['slug']
    #     productItem = get_object_or_404(prModel, slug=slug)
    #     context['product'] = productItem
    #
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     loaded_data = self.object
    #     request = self.request
    #     favorite_product_id = request.session['productID']
    #     context['isFavorite'] = favorite_product_id == str(loaded_data.id)
    #     return context


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


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST['productID']
        product = prModel.objects.get(id=product_id)
        request.session['productID'] = product_id
        return redirect(product.get_absolute_url())
