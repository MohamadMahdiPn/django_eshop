from django.db.models import Count, Max
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from Utils.Convertors import group_list
from site_module.models import SiteBanner
from .models import Product as prModel, ProductCategory, ProductBrand, Product, ProductVisit
from Utils.HttpService import get_client_ip
   
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

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        query = Product.objects.all()
        product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('start_price') or 10000000
        context['banners'] = SiteBanner.objects.filter(isActive=True,
                                                       position__iexact=SiteBanner.SiteBannerPosition.productList)

        nyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        grouped_list = []
        group_size = 4
        my_range = range(0, len(nyList), group_size)
        for i in my_range:
            grouped_list.append(nyList[i:i+group_size])
        return context

    def get_queryset(self):
        baseQuery = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        data = baseQuery.filter(isActive=True)

        request: HttpRequest = self.request
        start_price = request.GET.get('start')
        end_price = request.GET.get('end')
        if start_price is not None:
            data = data.filter(price__gte=start_price)
        if end_price is not None:
            data = data.filter(price__lte=end_price)

        if category_name is not None:
            data = data.filter(Category__url_title__iexact=category_name)
        if brand_name is not None:
            data = data.filter(brand__url_title__iexact=brand_name)
        return data


class ProductDetailsView(DetailView):
    template_name = 'product/ProductDetail.html'
    model = prModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        user_ip = get_client_ip(request=self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = ProductVisit.objects.filter(ipaddress__iexact=user_ip, product_id__exact=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductVisit(ipaddress=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()
        return context

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
