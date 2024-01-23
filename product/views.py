from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Product as prModel, ProductCategory, ProductBrand


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
    paginate_by = 5

    def get_queryset(self):
        baseQuery = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        data = baseQuery.filter(isActive=True)
        if category_name is not None:
            data = data.filter(Category__url_title__iexact=category_name)
        if brand_name is not None:
            data = data.filter(brand__url_title__iexact=brand_name)
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


def product_categories_component(request: HttpRequest):
    product_category = ProductCategory.objects.filter(is_Active=True, is_delete=False)
    return render(request, 'product/components/product_categories_component.html', {
        'categories': product_category
    })


def product_brands_component(request: HttpRequest):
    product_brand = ProductBrand.objects.annotate(product_count=Count('product')).filter(isActive=True)
    context = {
        'brands': product_brand
    }
    return render(request, 'product/components/product_brands_component.html', context)
