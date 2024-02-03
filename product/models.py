from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from account_module.models import User


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    is_Active = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


# class ProductInformation(models.Model):
#    color = models.CharField(max_length=200, verbose_name='color')
#    size = models.CharField(max_length=200, verbose_name='size')

#    def __str__(self):
#        return f"({self.color} - {self.size})"

#    class Meta:
#        verbose_name = 'اطلاعات کالا'
#        verbose_name_plural = 'اطلاعات کالا ها'

class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    isActive = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='عکس')
    title = models.CharField(max_length=300)
    price = models.IntegerField(verbose_name='قیمت')
    # rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    shortDescription = models.CharField(max_length=360, null=True)
    description = models.TextField(verbose_name='توصیحات اصلی')
    isActive = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    Category = models.ManyToManyField(ProductCategory, related_name='Categoties', verbose_name='دسته بندی ها')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)

    # product_information = models.OneToOneField(ProductInformation, on_delete=models.CASCADE,
    #                                           related_name='Product_info', verbose_name='additional Info', null=True)

    # product_tags = models.ManyToManyField(ProductTag, verbose_name='tags')

    def __str__(self):
        formatted_price = "{:,}".format(self.price)
        return f"{self.title}, ({formatted_price})"
        # return f"{self.title},({self.price})"

    def get_absolute_url(self):
        return reverse('productDetail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالا ها'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProductTags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.tag


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    ipaddress = models.CharField(max_length=30, verbose_name='Client ip')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name="کاربر ", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} -({self.ipaddress})'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول", related_name='products')
    image = models.ImageField(upload_to="productGallery", verbose_name="تصویر")
    isActive = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = 'تصاویر'
