from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('contactus', views.contact_page),
    # path('site-header' , views.site_header_partial, name='siteHeaderPartial')
]
