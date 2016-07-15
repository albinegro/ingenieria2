import os
from django.db import models
from customers.models import Customer
from django.core.validators import MinValueValidator
RANGE = (
		  (("1"),("1")),
		  (("2"),("2")),
		  (("3"),("3")),
		  (("4"),("4")),
		  (("5"),("5")),
		  (("6"),("6")),
		  (("7"),("7")),
		  (("8"),("8")),
		  (("9"),("9")),
		  (("10"),("10")))

# Create your models here.
class Hospedaje(models.Model):
	favoritos = models.ManyToManyField(Customer,blank=True, related_name="cus_favo")
	customer  = models.ForeignKey(Customer)
	titulo = models.CharField(max_length=250)
	ciudad = models.CharField(max_length=250)
	localidad = models.CharField(max_length=250)
	direccion = models.CharField(max_length=250)
	capacidad = models.IntegerField(validators=[MinValueValidator(1)])
	tipo = models.ForeignKey('TipoHospedaje')
	descripcion = models.TextField(max_length=250)
	estado = models.BooleanField(default=True)
	calificacion = models.CharField(default='0',max_length=2, null=True, blank=True)
	foto_1 = models.ImageField(upload_to='photos/', null=True, blank=True)
	foto_2 = models.ImageField(upload_to='photos/', null=True, blank=True)
	foto_3 = models.ImageField(upload_to='photos/', null=True, blank=True)
	foto_4 = models.ImageField(upload_to='photos/', null=True, blank=True)
	foto_5 = models.ImageField(upload_to='photos/', null=True, blank=True)


class TipoHospedaje(models.Model):
	descripcion = models.CharField(max_length=150)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.descripcion.encode('utf8')



class Preguntar(models.Model):
	hospedaje = models.ForeignKey(Hospedaje)
	customer = models.ForeignKey(Customer)
	fecha = models.DateField(auto_now_add=True)
	pregunta = models.TextField()
	respuesta = models.TextField(null=True, blank=True)
	visto = models.BooleanField(default=False)