from django.contrib.auth.models import AbstractUser , AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique=True, null=True, blank=True)
    email_active_code = models.CharField(max_length=11, unique=True, verbose_name='کد فعال سازی')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        return self.email