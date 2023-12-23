from django.shortcuts import render, get_object_or_404
from .models import Product as prModel
from .models import ProductCategory as prCategory
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.
def productList(request):
    # console = prCategory(title='Game console', url_title='gameConsole')
    # console.save()
    # ps_4 = prModel(title='Play station 4', price=16000000 , rating=4 , isActive=True , Category=console ,
    # shortDescription='PS 4') ps_4.save()

    products = prModel.objects.all().order_by('price')
    numberOfProducts = products.count()
    # averageRatings = products.aggregate(Avg("rating"), Min("price"))

    return render(request, 'product/productList.html', {
        'products': products,
        'totalNumberOfProducts': numberOfProducts,
        # 'averageRatings': averageRatings

    })


def productDetail(request, slug):
    # try:
    #    productItem = prModel.objects.get(id=productId)
    # except:
    #     raise Http404()

    productItem = get_object_or_404(prModel, slug=slug)
    return render(request, 'product/ProductDetail.html', {
        'product': productItem
    })
