from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class AccountManager(BaseUserManager):

    def create_user(self, username, password=None):
        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user


class Account(AbstractBaseUser):
    objects = AccountManager()

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
    )
    last_activity = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
