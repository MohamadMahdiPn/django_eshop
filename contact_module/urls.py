from django.urls import path
from . import views
urlpatterns = [
    # path('', views.contact_us_page, name='contact_us_page')
    path('', views.ContactView.as_view(), name='contact_us_page')
]