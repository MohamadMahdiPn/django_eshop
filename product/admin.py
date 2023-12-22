from django.contrib import admin
from . import models


# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductInfoAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = [
        # 'slug',
        'rating'
    ]
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = [
        '__str__', 'price', 'rating', 'isActive', 'Category', 'product_information'
    ]
    list_filter = ['price', 'rating', 'isActive', 'Category']
    list_editable = ['price', 'rating', 'isActive', 'Category', 'product_information']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.ProductInformation, ProductInfoAdmin)
