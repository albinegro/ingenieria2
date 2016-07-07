# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, User)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


TIPOS_TARJETAS = (

        (("visa"),("Visa")),
        (("mastercard"),("MasterCard")),
        (("american"),("AmericanExpress")),
        (("naranja"),("Naranja")),
        (("cabal"),("CABAL")),
        (("tarjeta_shopping"),("TarjetaShopping")),
        (("argencard"),("ArgenCard")),
        (("cencosud"),("Cencosud")),

    
        )
CIVIL = (

        (("soltero/a"),("Soltero/a")),
        (("casado/a"),("Casado/a")),
        (("viudo/a"),("Viudo/a")),
        )

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
        user.fecha_n = datetime.datetime.now()
        user.direccion = "admin"
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser, PermissionsMixin):

    tarjeta= models.ForeignKey('Tarjeta', null=True, blank=True)
    nombre = models.CharField(_('Nombre'), max_length=30)
    apellido = models.CharField(_('Apellido'), max_length=30)
    email = models.EmailField('Correo Electrónico', unique=True)
    admin = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    cliente = models.BooleanField(default=False)
    tel = models.IntegerField('Teléfono', null=True, blank=True)
    estado_civil = models.CharField(_('Estado Civil'),max_length=50,choices=CIVIL, null=True, blank=True)
    direccion = models.CharField('Dirección',max_length=30)
    religion = models.CharField('Religión',max_length=30,  null=True, blank=True)
    temp_pass = models.BooleanField(default=False)
    fecha_premium = models.DateTimeField(null=True, blank=True)
    fecha_n = models.DateField(_('Fecha Nacimiento'), null=True, blank=True)
    code_postal = models.IntegerField('Código Postal', null=True, blank=True,  validators=[
            MinValueValidator(1000)
        ])
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = False

    def get_short_name(self):
        return self.email
 
class Tarjeta(models.Model):
    tarjeta_credito = models.IntegerField(validators=[
            MinValueValidator(1000000000000000)
        ])
    tipo_tarjeta = models.CharField(max_length=250, choices=TIPOS_TARJETAS)
    fecha_venc_tarjeta = models.DateField()
    codigo_seguridad = models.IntegerField(validators=[
            MinValueValidator(100)
        ])
    premiun_pago = models.CharField(max_length=14)
        
class Calificacion(models.Model):
    """docstring for Calificacion"""
    inquilino = models.ForeignKey(Customer,related_name="inqui")
    propietario = models.ForeignKey(Customer,related_name="propie")
    comentario_i  = models.TextField(null=True,blank=True)
    comentario_p = models.TextField(null=True,blank=True)
    i_puntos = models.IntegerField(null=True,blank=True)
    p_putnos = models.IntegerField(null=True,blank=True)

       





