from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProductInformation(models.Model):
    color = models.CharField(max_length=200 , verbose_name='color')
    size = models.CharField(max_length=200 , verbose_name='size')

    def __str__(self):
        return f"({self.color} - {self.size})"

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    shortDescription = models.CharField(max_length=360, null=True)
    isActive = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    Category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE , null= True,related_name='Categoties')
    product_information = models.OneToOneField(ProductInformation, on_delete=models.CASCADE, related_name='Product_info', verbose_name='additional Info', null=True)

    def __str__(self):
        return f"{self.title} ({self.price})"

    def get_absolute_url(self):
        return reverse('productDetail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

