from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
import os
from django.core.exceptions import ValidationError




def validate_files(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Yuklanayotgan fayl formati .png, .jpg bo'lishi shart !!!")




class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    plus_ball = models.IntegerField(default=0, null=True, blank=True)
    minus_ball = models.IntegerField(default=0, null=True, blank=True)
    images = models.ImageField(upload_to="images/",  blank=True, null=True, validators=[validate_files])
    user_number = models.IntegerField(default=0)

    def total_point(self):
        return self.plus_ball - self.minus_ball



    def __str__(self):
        return f"{self.username}"


    class Meta:
        verbose_name="Hodimlar_"