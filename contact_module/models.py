from django.db import models


# Create your models here.
class contactUser(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    fullName = models.CharField(max_length=300, verbose_name='نام و نشان')
    message = models.TextField(max_length=300, verbose_name='پیام')
    isRead = models.BooleanField(default=False, verbose_name='خوانده شده')
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updatedDate = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    responseText = models.TextField(verbose_name='پاسخ ادمین', null=True, blank=True)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return f'{self.title} ({self.fullName})'
