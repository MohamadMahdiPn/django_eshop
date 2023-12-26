from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import reverse

from contact_module.forms import ContactForm


# Create your views here.
def contact_us_page(request):
    # contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse('index'))
    else:
        contact_form = ContactForm()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})
