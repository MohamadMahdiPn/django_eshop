from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.views import View
from django.views.generic.edit import FormView
# from django.views.generic import
from contact_module.forms import ContactForm, ContactUserModelForm
from contact_module.models import contactUser


class ContactView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUserModelForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)


    # def get(self, request):
    #     contact_form = ContactUserModelForm()
    #     return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})

    # def post(self, request):
    #     form = ContactUserModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('index'))


# Create your views here.
def contact_us_page(request):
    if request.method == 'POST':
        form = ContactUserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    contact_form = ContactUserModelForm()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})
