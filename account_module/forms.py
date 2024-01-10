from django import forms
from django.core import validators


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        required=True, label='Email',
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ])
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True,
        error_messages={'required': 'Pass is required'},
        validators=[
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(100)

        ]
    )


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        required=True, label='Email',
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ])


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True,
        error_messages={'required': 'Pass is required'})

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Re type Password',
        required=True,
        error_messages={'required': 'ReType is required'})


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='Email',
        required=True,
        error_messages={'required': 'Email is required'},
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,

        ])

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True,
        error_messages={'required': 'Pass is required'})

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Re type Password',
        required=True,
        error_messages={'required': 'ReType is required'})

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('رمز و تکرار یکی نیست')
        return confirm_password
