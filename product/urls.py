from django.urls import path
from . import views

urlpatterns = [
    # path('', views.productList),
    path('',views.ProductListView.as_view(),name='product-list'),
    path('cat/<cat>',views.ProductListView.as_view(),name='product-categories-list'),
    path('brand/<brand>', views.ProductListView.as_view(),name='product-list-by-brands'),
    path('<slug:slug>', views.ProductDetailsView.as_view(), name='productDetail'),
    path('productFavorite', views.AddProductFavorite.as_view(), name='productFavorite'),

]
