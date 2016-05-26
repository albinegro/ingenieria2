from django.forms import ModelForm
from django import forms
from .models import Customer, Tarjeta, TIPOS_TARJETAS
from django.core.validators import MaxValueValidator


class TarjetaForm(ModelForm):
	class Meta:
		model = Tarjeta
		exclude =['premiun_pago']


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ["nombre",
				 "apellido",
				 "correo", 
				 "password",
				 "tel",
				 "direccion",
				 "code_postal"
		]

	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		self.fields['correo'].widget = forms.EmailInput(attrs={
			'placeholder': 'nombre@ejemplo.com'})

class CustomerDateForm(CustomerForm):
	ano = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1970,2018)])
	mes = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,13)])
	dia = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,32)])




class PremiumForm(CustomerForm):
	tarjeta_credito = forms.CharField()
	tipo_tarjeta = forms.ChoiceField(choices=TIPOS_TARJETAS)
	fecha_venc_tarjeta = forms.DateField()
	codigo_seguridad = forms.IntegerField(max_value=999)




