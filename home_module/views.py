from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from site_module.models import SiteSetting


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
    setting = SiteSetting.objects.filter(is_main_setting=True).first()

    return render(request, 'shared/siteHeaderPartial.html', {
        'site_setting': setting
    })


def site_footer_partial(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    return render(request, 'shared/siteFooterPartial.html', {
        'site_setting': setting
    })