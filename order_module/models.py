from django.db import models
from account_module.models import User
from product.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users',verbose_name="کاربر")
    isPaid = models.BooleanField(default=False, verbose_name="نهایی شده / نشده")
    payment_date = models.DateField(null=True,blank=True,verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید"

    def __str__(self):
        return str(self.user)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders',verbose_name="سفارش")
    quantity = models.IntegerField(verbose_name="تعداد",null=True,blank=True,default=0)
    final_price = models.IntegerField(verbose_name="مبلغ نهایی",null=True,blank=True,default=0)

    class Meta:
        verbose_name = "کالای سفارش"
        verbose_name_plural = "کالاهای سفارش"

    def __str__(self):
        return str(self.product.name)