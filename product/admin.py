from django.contrib import admin
from . import models


# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductTagAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'Category', 'isActive']
    list_display = ['title', 'price', 'isActive','slug']
    list_editable = [ 'price', 'isActive']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
# admin.site.register(models.ProductInformation, ProductInfoAdmin)
admin.site.register(models.ProductTag, ProductTagAdmin)
