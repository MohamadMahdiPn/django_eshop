from django.contrib import admin
from . import models
# Register your models here.


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'url_title', 'is_Active']
    list_editable = ['url_title', 'is_Active']


admin.site.register(models.SiteSetting)
admin.site.register(models.FooterLink, FooterLinkAdmin)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.Slider, SliderAdmin)