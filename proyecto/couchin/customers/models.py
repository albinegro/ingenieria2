from django.db import models

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, User)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import datetime

TIPOS_TARJETAS = (

        (("visa"),("Visa")),
        (("mastercard"),("MasterCard")),
    
        )


# Create your models here.
class UserManager(BaseUserManager):

    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(is_active=True)

    def create_user(self, correo, password=None):
        if not correo:
            raise ValueError('Users must have an email address')

        user = self.model(
            correo=self.normalize_email(correo),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password):
        user = self.create_user(correo, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.admin = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    tarjeta= models.ForeignKey('Tarjeta', null=True)
    nombre = models.CharField(_('Nombre'), max_length=30)
    apellido = models.CharField(_('Apellido'), max_length=30)
    correo = models.EmailField(_('Correo Electronico'), unique=True)
    admin = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    cliente = models.BooleanField(default=False)
    tel = models.CharField(_('Telefono'),max_length=14, null=True, blank=True)
    direccion = models.CharField(max_length=30)
    fecha_premium = models.DateTimeField(null=True, blank=True)
    fecha_n = models.DateField(_('Fecha Nacimiento'), null=True, blank=True )
    code_postal = models.CharField(_('Codigo Postal'),max_length=10)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = False

    def get_short_name(self):
        return self.correo
 
class Tarjeta(models.Model):
    tarjeta_credito = models.CharField(max_length=16)
    tipo_tarjeta = models.CharField(max_length=250, choices=TIPOS_TARJETAS)
    fecha_venc_tarjeta = models.DateField()
    codigo_seguridad = models.CharField(max_length=3)
    premiun_pago = models.CharField(max_length=14)
        
class Calificacion(models.Model):
    """docstring for Calificacion"""
    
       





