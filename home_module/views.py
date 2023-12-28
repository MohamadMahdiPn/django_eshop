from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data From home page'
        return context
    # def get(self, request):
    #     return render(request, 'home_module/index_page.html')


def site_header_partial(request):
    return render(request, 'shared/siteHeaderPartial.html', {})


def site_footer_partial(request):
    return render(request, 'shared/siteFooterPartial.html', {})