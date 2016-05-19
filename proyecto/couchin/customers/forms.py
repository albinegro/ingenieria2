from django.forms import ModelForm
from django import forms
from .models import Customer, Tarjeta, TIPOS_TARJETAS


class TarjetaForm(ModelForm):
	class Meta:
		model = Tarjeta
		exclude =["client"]


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ["nombre",
			     "apellido",
			     "correo", 
			     "password",
			     "tel",
			     "direccion",
			     "fecha_n",
			     "code_postal"
		]



class PremiumForm(CustomerForm):
	tarjeta_credito = forms.CharField()
	tipo_tarjeta = forms.ChoiceField(choices=TIPOS_TARJETAS)
	fecha_venc_tarjeta = forms.DateField()
	codigo_seguridad = forms.IntegerField(max_value=999)




