from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = [
        #'slug',
        'rating'
    ]
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(models.Product, ProductAdmin)
