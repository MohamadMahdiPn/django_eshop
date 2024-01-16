from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=50, verbose_name='نام سایت')
    site_url = models.URLField(verbose_name='دامنه سایت')
    about_us_txt = models.TextField(verbose_name='درباره ما')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='آدرس')
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


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی فوتر'
        verbose_name_plural = 'دسته بندی های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    url = models.URLField(max_length=255, verbose_name='لینک')
    footerLinkBox = models.ForeignKey(FooterLinkBox, verbose_name=' دسته بندی', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ' لینک فوتر'
        verbose_name_plural = ' لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    url = models.URLField(max_length=255, verbose_name='لینک')
    url_title = models.CharField(max_length=255, verbose_name='عنوان لینک')
    image = models.ImageField(upload_to='images/slider', null=True, blank=True, verbose_name='عکس')
    is_Active = models.BooleanField(verbose_name='فعال', default=True)

    class Meta:
        verbose_name = 'تصویر اسلایدر'
        verbose_name_plural = 'تصاویر اسلابدر'

    def __str__(self):
        return self.title