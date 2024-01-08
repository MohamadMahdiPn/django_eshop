from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import View
from django.urls import reverse
from django.views.generic import CreateView
from .models import User
from django.utils.crypto import get_random_string
from account_module.forms import RegistrationForm


# Create your views here.

class LoginView(View):
    def get(self, request):

        context = {
            'register_form': None
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        pass

class RegisterView(View):
    def get(self, request):
        register_form = RegistrationForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'This email is already taken.')
            else:
                new_user = User(email=user_email, email_active_code=get_random_string(48), is_active=False, username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                #todo: send email
                return redirect(reverse('login_page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)
