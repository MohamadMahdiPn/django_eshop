from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('edit-profile', views.EditUserProfile.as_view(),name='edit_profile_page'),
    path('change-Password', views.ChangePasswordPage.as_view(),name='change_password_page')
]