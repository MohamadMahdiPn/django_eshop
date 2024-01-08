from django import forms
from django.core import validators



class RegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='Email',
        required=True,
        error_messages={'required': 'Email is required'},
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,

        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True,
        error_messages={'required': 'Pass is required'})
    confirm_password = forms.CharField()

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('رمز و تکرار یکی نیست')
        return confirm_password
