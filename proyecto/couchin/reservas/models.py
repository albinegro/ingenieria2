from django.db import models
from customers.models import Customer
from hospedajes.models import Hospedaje

# Create your models here.


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
