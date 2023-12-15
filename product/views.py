from django.shortcuts import render, get_object_or_404
from .models import Product as prModel
from django.http import Http404


# Create your views here.
def productList(request):
    products = prModel.objects.all()
    return render(request, 'product/productList.html', {
        'products': products
    })


def productDetail(request, productId):
   # try:
    #    productItem = prModel.objects.get(id=productId)
    #except:
   #     raise Http404()
    productItem = get_object_or_404(prModel, id=productId)
    return render(request, 'product/ProductDetail.html', {
        'product': productItem
    })
