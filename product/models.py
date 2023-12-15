from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    shortDescription = models.CharField(max_length=360)
    isActive = models.BooleanField()

    def __str__(self):
        return f"{self.title} ({self.price})"

    def get_absolute_url(self):
        return reverse('productDetail',args=[self.id])
