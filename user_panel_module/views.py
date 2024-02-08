from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView

from order_module.models import Order
from .forms import EditProfileModelForm, ChangePasswordForm
from account_module.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
# Create your models here.


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


class ChangePasswordPage(View):
    def get(self, request: HttpRequest):

        return render(request, 'user_panel_module/change_password_page.html', {
            'form': ChangePasswordForm()
        })

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cUser = User.objects.filter(id=request.user.id).first()
            if cUser.check_password(form.cleaned_data.get('current_password')):
                cUser.set_password(form.cleaned_data.get('password'))
                cUser.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('current_password', 'کلمه عبور اشتباه است')
        return render(request, 'user_panel_module/change_password_page.html', {
            'form': ChangePasswordForm()
        })


class EditUserProfile(View):
    def get(self, request: HttpRequest):
        # edit_form = EditProfileModelForm(initial={
        #     'first_name': request.user.first_name,
        #     'last_name': request.user.last_name,
        #     'address': request.user.address
        # })
        cUser = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=cUser)
        context = {
            'form': edit_form,
            'current_user': cUser
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        cUser = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES,instance=cUser)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


def remove_order_detail(request):
    current_order, created = Order.objects.prefetch_related('orders').get_or_create(isPaid=False,user_id=request.user.id)
    detail_id = request.GET.get('detail_id')
    detail = current_order.orders.filter(id=detail_id).first()
    if detail is None:
        return JsonResponse({
            'status': 'not_found_detail'
        })
    detail.delete()

    total_amount = 0
    for order_detail in current_order.orders.all().exclude(id=detail_id):
        total_amount += order_detail.product.price * order_detail.quantity
    context = {
            "order": current_order,
            'sum': total_amount
        }
    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })


@login_required
def user_basket(request: HttpRequest):
    user_open_order, created = Order.objects.prefetch_related('orders').get_or_create(isPaid=False, user_id=request.user.id)
    total_amount = 0
    for order_detail in user_open_order.orders.all():
        total_amount += order_detail.product.price * order_detail.quantity
    context = {
        "order": user_open_order,
        'sum': total_amount
    }
    return render(request, 'user_panel_module/user_basket.html',context)


@login_required
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')