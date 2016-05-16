from django.db import models

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, User)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import datetime

# Create your models here.
class UserManager(BaseUserManager):

    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(is_active=True)

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.admin = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    #username = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    client_premium = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    client = models.BooleanField(default=False)
    date_premium = models.DateTimeField()
    premiun_pay = models.CharField(max_length=14)
    email = models.EmailField(_('email address'),unique=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    date_emision = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=20)
    registration = models.CharField(max_length=1, null=True, blank=True)
    name_registration = models.CharField(max_length=20, null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    objects = UserManager()
    all_objects = models.Manager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []





