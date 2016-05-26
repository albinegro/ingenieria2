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


class Foto(models.Model):
	hospedaje = models.ForeignKey(Hospedaje)
	foto = models.ImageField(upload_to="hospedaje")

class TipoHospedaje(models.Model):
	descripcion = models.CharField(max_length=150)
	activo = models.BooleanField(default=True)

class Comentario(models.Model):
	hospedaje = models.ForeignKey(Hospedaje)
	customer = models.ForeignKey(Customer)
	fecha = models.DateTimeField()
	pregunta = models.TextField()
	respuesta = models.TextField()