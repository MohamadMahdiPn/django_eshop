from django.urls import path
from . import views

urlpatterns = [
    path('', views.productList),
    path('<slug:slug>', views.productDetail, name='productDetail'),
]
