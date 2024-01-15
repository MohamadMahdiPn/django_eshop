from django.db import models

# Create your models here.
class SieSetting(models.Model):
    site_name = models.CharField(max_length=50, verbose_name='نام سایت')
    site_url = models.URLField(verbose_name='دامنه سایت')
    about_us_txt = models.TextField(verbose_name='درباره ما')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی')
    address = models.CharField(max_length=255, null=True, blank=True , verbose_name='آدرس')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='شماره تماس')
    fax = models.CharField(max_length=15, null=True, blank=True, verbose_name='فکس')
    email = models.EmailField(max_length=150, null=True, blank=True, verbose_name='ایمیل')
    site_logo = models.ImageField(upload_to='images/setting', null=True, blank=True, verbose_name='لوگو')
    copyright = models.CharField(max_length=50, null=True, blank=True, verbose_name='کپی رایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name
