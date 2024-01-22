from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import EditProfileModelForm
from account_module.models import User
# Create your models here.


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')


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



