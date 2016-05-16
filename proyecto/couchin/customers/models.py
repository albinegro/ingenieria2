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
    nombre = models.CharField(_('first name'), max_length=30)
    apellido = models.CharField(_('last name'), max_length=30)
    correo = models.EmailField(_('email address'), blank=True, unique=True)
    admin = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    cliente = models.BooleanField(default=False)
    tel = models.CharField(max_length=14, null=True, blank=True)
    direccion = models.CharField(max_length=30)
    fecha_premium = models.DateTimeField()
    premiun_pago = models.CharField(max_length=14)
    fecha_n = models.DateField()
    zip_code = models.CharField(max_length=10)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['correo']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True
 

class Calificacion(object):
    """docstring for Calificacion"""
       





