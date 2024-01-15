from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import View
from django.urls import reverse
from django.views.generic import CreateView
from .models import User
from django.utils.crypto import get_random_string
from account_module.forms import RegistrationForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from django.http import Http404, HttpRequest
from django.contrib.auth import login, authenticate, logout
from Utils.EmailService import sendEmail
# Create your views here.


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            userEmail = login_form.cleaned_data.get('email')
            userPass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=userEmail).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'Account is disabled.')
                else:
                    passIsValid: bool = user.check_password(userPass)
                    if passIsValid:
                        login(request, user)
                        return redirect(reverse('index'))
                    else:
                        login_form.add_error('email', 'Account not found')
            else:
                login_form.add_error('email', 'Account not found')
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


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
                new_user = User(email=user_email, email_active_code=get_random_string(48), is_active=False,
                                username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                sendEmail("Account Created",new_user.email,{'username': new_user.username}, 'emails/activate_account.html')
                return redirect(reverse('login_page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(48)
                user.save()
                # todo: show success page
                return redirect(reverse('login_page'))
            else:
                # todo: show failed page
                pass
        raise Http404


class ForgotPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgetPasswordForm()
        return render(request, 'account_module/ForgotPassword.html', {
            'forget_pass_form': forget_pass_form
        })

    def post(self, request: HttpRequest):

        forget_pass_form = ForgetPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            userEmail = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=userEmail).first()
            if user is not None:
                # send reset pass in email
                pass

        return render(request, 'account_module/ForgotPassword.html', {
            'forget_pass_form': forget_pass_form
        })


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            redirect(reverse('login_page'))

        resetPasswordForm = ResetPasswordForm()
        context = {
            'reset_pass_form': resetPasswordForm,
            'User_active_code': user.email_active_code
        }
        return render(request, 'account_module/ResetPassword.html', context)

    def post(self, request: HttpRequest, active_code):
        resetPasswordForm = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if resetPasswordForm.is_valid():

            if user is None:
                return redirect(reverse('login_page'))
            newUserPassword = resetPasswordForm.cleaned_data.get('password')
            user.set_password(newUserPassword)
            user.email_active_code = get_random_string(48)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        return render(request, 'account_module/ResetPassword.html', {
            'reset_pass_form': resetPasswordForm,
            'User_active_code': user.email_active_code
        })

class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(reverse('login_page'))
