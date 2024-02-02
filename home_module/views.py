from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView
from Utils.Convertors import group_list
from product.models import Product, ProductCategory
from site_module.models import SiteSetting, FooterLinkBox, Slider


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data From home page'
        context['Sliders'] = Slider.objects.filter(is_Active=True)

        latest_products = Product.objects.filter(isActive=True).order_by('-id')[:12]
        context['latest_products'] = group_list(latest_products, 2)

        most_visited_products = Product.objects.filter(isActive=True,).annotate(visit_count=Count('productvisit')).order_by('productvisit')[:12]
        context['most_visited_products'] = group_list(most_visited_products, 2)

        categories = list(ProductCategory.objects.annotate(products_count=Count('Categoties')).filter(is_Active=True, is_delete=False, products_count__gt=0)[:6])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.Categoties.all()[:4])
            }
            categories_products.append(item)
        context['categories_Products'] = categories_products
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
    footerLinkBoxes = FooterLinkBox.objects.all()
    for item in footerLinkBoxes:
        item.footerlink_set.all()
    return render(request, 'shared/siteFooterPartial.html', {
        'site_setting': setting,
        'footerLinkBoxes': footerLinkBoxes
    })


class AboutUsView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        site_setting:SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context

