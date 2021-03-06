from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', )

    objects = BaseUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
