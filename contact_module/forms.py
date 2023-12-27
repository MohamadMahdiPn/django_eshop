from django import forms
from .models import contactUser


class ContactForm(forms.Form):
    fullName = forms.CharField(max_length=300, required=True, error_messages={
        'required': 'اطلاعات کامل شود'
    },
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "نام"}),
                               label='نام و نام خانوادگی')
    email = forms.EmailField(required=True, label='ایمیل',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=200,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "نام"}),
                              label='موضوع')
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'توضیحات',
                                                        'cols': '40',
                                                        'rows': '5',
                                                        'id': 'message'
                                                        }), label='توضیحات')


class ContactUserModelForm(forms.ModelForm):
    class Meta:
        model = contactUser
        fields = ['fullName', 'email', 'message', 'title']
        # fields = '__all__'
        # exclude = ['createdDate']
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "نام"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'توضیحات',
                                             'cols': '40',
                                             'rows': '5',
                                             'id': 'message'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "موضوع"})

        }