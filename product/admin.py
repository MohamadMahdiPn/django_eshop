from django.contrib import admin
from . import models


# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductTagAdmin(admin.ModelAdmin):
    pass


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['title',  'isActive']
    list_editable = ['isActive']


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'Category', 'isActive']
    list_display = ['title', 'price', 'isActive','slug']
    list_editable = ['price', 'isActive']

# class ProductVisitAdmin(admin.ModelAdmin):
#     list_display = []



admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
# admin.site.register(models.ProductInformation, ProductInfoAdmin)
admin.site.register(models.ProductTag, ProductTagAdmin)
admin.site.register(models.ProductBrand, ProductBrandAdmin)
admin.site.register(models.ProductVisit)