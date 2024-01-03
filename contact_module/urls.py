from django.urls import path
from . import views
urlpatterns = [
    # path('', views.contact_us_page, name='contact_us_page')
    path('', views.ContactView.as_view(), name='contact_us_page'),
    path('createProfile/', views.CreateProfileView.as_view(), name='create_profile_page')
]