from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.views import View

from contact_module.forms import ContactForm, ContactUserModelForm
from contact_module.models import contactUser


class ContactView(View):
    def get(self, request):
        contact_form = ContactUserModelForm()
        return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})

    def post(self, request):
        form = ContactUserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))


# Create your views here.
def contact_us_page(request):
    # contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        # form = ContactForm(request.POST)
        form = ContactUserModelForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # contactDb = contactUser(form.cleaned_data)
            # fullName=form.cleaned_data['fullName'],
            # email=form.cleaned_data['email'],
            # message=form.cleaned_data['text'],
            # isRead=False,
            # title=form.cleaned_data['subject']
            # )
            form.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        contact_form = ContactUserModelForm()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})
