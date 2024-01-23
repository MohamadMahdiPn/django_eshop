from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
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


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')