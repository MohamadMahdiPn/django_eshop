from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index_page, name='index'),
    path('', views.HomeView.as_view(), name='index'),
    path('Aboutus', views.AboutUsView.as_view(), name='AboutUs'),
    # path('contactus', views.contact_page),
    # path('site-header' , views.site_header_partial, name='siteHeaderPartial')
]
