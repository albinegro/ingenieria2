# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Customer, Tarjeta, TIPOS_TARJETAS
from django.core.validators import MaxValueValidator


class TarjetaForm(ModelForm):
	class Meta:
		model = Tarjeta
		exclude =['premiun_pago', 'fecha_venc_tarjeta']

	def __init__(self, *args, **kwargs):
		super(TarjetaForm, self).__init__(*args, **kwargs)
		self.fields['tarjeta_credito'].widget = forms.NumberInput(attrs={
			'maxlength': 16})
		self.fields['codigo_seguridad'].widget =forms.NumberInput(attrs={
			 'maxlength':3})



class TarjetaDateForm(TarjetaForm):
	ano = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(2016,2028,2)],label="Año")
	mes = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,13)])



class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ["nombre",
				 "apellido",
				 "email", 
				 "password",
				 "tel",
				 "direccion",
				 "code_postal"
		]

	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget = forms.EmailInput(attrs={
			'placeholder': 'nombre@ejemplo.com'})
		self.fields['password'].widget = forms.PasswordInput()
		self.fields['tel'].widget =forms.NumberInput(attrs={'maxlength':14})
		self.fields['code_postal'].widget =forms.NumberInput(attrs={'maxlength':4})

class CustomerDateForm(CustomerForm):
	ano = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1970,2018)], label="Año")
	mes = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,13)])
	dia = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,32)])


class CustomerEditForm(ModelForm):
	class Meta:
		model = Customer
		fields = ["nombre",
				 "apellido",
				 "email", 
				 "tel",
				 "direccion",
				 "code_postal"
		]

	def __init__(self, *args, **kwargs):
		super(CustomerEditForm, self).__init__(*args, **kwargs)
		self.fields['tel'].widget =forms.NumberInput(attrs={'maxlength':14})
		self.fields['code_postal'].widget =forms.NumberInput(attrs={'maxlength':4})

class CustomerDateEditForm(CustomerEditForm):
	ano = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1970,2018)], label="Año")
	mes = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,13)])
	dia = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,32)])




class PremiumForm(CustomerForm):
	tarjeta_credito = forms.CharField()
	tipo_tarjeta = forms.ChoiceField(choices=TIPOS_TARJETAS)
	fecha_venc_tarjeta = forms.DateField()
	codigo_seguridad = forms.IntegerField(max_value=999)




