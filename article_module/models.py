from django.db import models
from account_module.models import User
from jalali_date import datetime2jalali, date2jalali
# Create your models here.


class ArticleCategory(models.Model):
    parent = models.ForeignKey('self',null=True,blank=True , on_delete=models.CASCADE, verbose_name="والد")
    title = models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name="عنوان")
    urlTitle = models.CharField(max_length=200,verbose_name="عنواد آدرس")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی مقاله ها"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="عنوان در url", allow_unicode=True)
    image = models.ImageField(upload_to='articles', verbose_name="تصویر", blank=True, null=True)
    description = models.TextField(verbose_name="توضیحات", blank=True, null=True)
    short_description = models.TextField(verbose_name="توضیحات", blank=True, null=True)
    text = models.TextField(verbose_name="متن اصلی")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name="دسته بندی ها")
    author = models.ForeignKey(User, verbose_name="نویسنده", on_delete=models.CASCADE, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def get_jalali_date(self):
        return date2jalali(self.created_at)

    def get_time(self):
        return self.created_at.strftime('%H:%M')
