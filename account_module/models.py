from django.contrib.auth.models import AbstractUser , AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique=True, null=True, blank=True)
    email_active_code = models.CharField(max_length=11, unique=True,verbose_name='کد فعال سازی')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email