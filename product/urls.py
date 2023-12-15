from django.urls import path
from . import views

urlpatterns = [
    path('', views.productList),
    path('<int:productId>', views.productDetail , name='productDetail'),
]
