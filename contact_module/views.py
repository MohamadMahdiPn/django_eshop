from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView , CreateView
from django.views.generic import ListView
# from django.views.generic import
from contact_module.forms import ContactForm, ContactUserModelForm, ProfileForm
from contact_module.models import contactUser, UserProfile
from site_module.models import SiteSetting


class ContactView(FormView):

    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUserModelForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context

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


def store_file(file):
    with open(f'temp/{file}', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/createProfile/'

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#
#         return render(request, 'contact_module/create_profile_page.html', {
#             'form': form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             # store_file(request.FILES['user_image'])
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return redirect('/contact-us/createProfile/')
#         return render(request, 'contact_module/create_profile_page.html', {
#             'form': submitted_form
#         })

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'