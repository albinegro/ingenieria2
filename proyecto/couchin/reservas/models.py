from django.db import models
from customers.models import Customer
from hospedajes.models import Hospedaje

# Create your models here.

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


STATE_RESERVA = ((("pendiente"), ("Pendiente")),
                 (("rechazada"), ("Rechazada")),
                 (("finalizada"), ("Finalizada")),
                 (("aceptada"), ("Aceptada")))

class Reserva(models.Model):
	hospedaje = models.ForeignKey(Hospedaje,related_name="imueble")
	inquilino = models.ForeignKey(Customer,related_name="inquilino")
	dueno = models.ForeignKey(Customer, related_name="dueno")
	estado = models.CharField(choices=STATE_RESERVA, default="pendiente", max_length=30)
	fecha_desde = models.DateField()
	fecha_hasta = models.DateField()
	vista = models.BooleanField(default=False)
	califica_dueno = models.ForeignKey('Calificacion', related_name="cal_dueno", blank=True, null=True)
	califica_inquilino = models.ForeignKey('Calificacion', related_name="cal_inquilino", blank=True, null=True)


class Calificacion(models.Model):
	descripcion = models.TextField(max_length=250)
	numero = models.CharField(choices=RANGE, default="1", max_length=30)