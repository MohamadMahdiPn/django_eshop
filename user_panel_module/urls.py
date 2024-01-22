from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('edit_profile', views.EditUserProfile.as_view(),name='edit_profile_page')
]