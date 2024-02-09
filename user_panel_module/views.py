from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView,ListView
from django.utils.decorators import method_decorator
from order_module.models import Order, OrderItem
from .forms import EditProfileModelForm, ChangePasswordForm
from account_module.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
# Create your models here.


@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class myShoppings(ListView):
    model = Order
    template_name = 'user_panel_module/user_shopping.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        request: HttpRequest = self.request
        queryset = queryset.filter(user_id=request.user.id,isPaid=True)
        return queryset


@login_required
def remove_order_detail(request):

    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })
    deleted_count, deleted_dict = OrderItem.objects.filter(id=detail_id, order__isPaid=False, order__user_id=request.user.id).delete()
    if deleted_count == 0:
        return JsonResponse({
            'status': 'not_found_detail'
        })
    current_order, created = Order.objects.prefetch_related('orders').get_or_create(isPaid=False,
                                                                                    user_id=request.user.id)
    total_amount = current_order.calculateTotalPrice()
    context = {
            "order": current_order,
            'sum': total_amount
        }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


@login_required
def change_order_detail(request):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    orderDetail = OrderItem.objects.filter(id=detail_id, order__user_id=request.user.id, order__isPaid=False).first()
    if orderDetail is None:
        return JsonResponse({
            'status': 'not_found'
        })

    if state == 'increase':
        orderDetail.quantity += 1
        orderDetail.save()
    elif state == 'decrease':
        if orderDetail.quantity ==1:
            orderDetail.delete()
        else:
            orderDetail.quantity -= 1
            orderDetail.save()
    else:
        return JsonResponse({
            'status': 'error'
        })
    current_order, created = Order.objects.prefetch_related('orders').get_or_create(isPaid=False,
                                                                                    user_id=request.user.id)
    total_amount = current_order.calculateTotalPrice()
    context = {
        "order": current_order,
        'sum': total_amount
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
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


def my_Shopping_Details(request: HttpRequest,order_id):
    order = Order.objects.filter(id=order_id, user_id=request.user.id).first()
    if order is None:
        raise Http404('سبد یافت نشد')

    return render(request, 'user_panel_module/user_shopping_detail.html',{
        'order': order
    })