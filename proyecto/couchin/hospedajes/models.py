import os
from django.db import models
from customers.models import Customer

# Create your models here.
class Hospedaje(models.Model):
	customer  = models.ForeignKey(Customer)
	localidad = models.CharField(max_length=250)
	ciudad = models.CharField(max_length=250)
	direccion = models.CharField(max_length=250)
	capacidad = models.IntegerField()
	descripcion = models.TextField(max_length=250)
	titulo = models.CharField(max_length=250)
	tipo = models.ForeignKey('TipoHospedaje')
	estado = models.BooleanField(default=True)
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

#class Comentario(models.Model):
#	hospedaje = models.ForeignKey(Hospedaje)
#	customer = models.ForeignKey(Customer)
#	fecha = models.DateTimeField()
#	pregunta = models.TextField()
#	respuesta = models.TextField()