from django.urls import path
from . import views

urlpatterns = [
    # path('', views.productList),
    path('',views.ProductListView.as_view()),
    path('<slug:slug>', views.ProductDetailsView.as_view(), name='productDetail'),
]
