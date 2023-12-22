from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, 'home_module/index_page.html')


def contact_page(request):
    return render(request, 'home_module/contactPage.html')


def site_header_partial(request):
    return render(request, 'shared/siteHeaderPartial.html', {})


def site_footer_partial(request):
    return render(request, 'shared/siteFooterPartial.html', {})