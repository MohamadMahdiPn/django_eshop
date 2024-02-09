from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('edit-profile', views.EditUserProfile.as_view(),name='edit_profile_page'),
    path('change-Password', views.ChangePasswordPage.as_view(),name='change_password_page'),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('my-shoppings', views.myShoppings.as_view(), name='my_shopping_page'),
    path('my-shoppings-details/<order_id>', views.my_Shopping_Details, name='my_shopping_details_page'),
    path('remove-order', views.remove_order_detail, name='remove-order'),
    path('change-order', views.change_order_detail, name='change-order'),
]