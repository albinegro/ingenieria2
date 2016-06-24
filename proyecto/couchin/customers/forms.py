# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Customer, Tarjeta, TIPOS_TARJETAS
from django.core.validators import MaxValueValidator


class TarjetaForm(ModelForm):
	codigo_seguridad = forms.IntegerField(error_messages={'invalid':"Ingrese un código de seguridad válido", 'min_value':'Ingrese un código de 3 caracteres'})
	tarjeta_credito = forms.IntegerField(error_messages={'invalid':"Ingrese un número de tarjeta válido", 'min_value':'Ingrese un código de 16 caracteres'})
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
	ano = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(2017,2028,1)],label="Año")
	mes = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,13)])



class CustomerForm(ModelForm):
	code_postal = forms.IntegerField(label="Código Postal",error_messages={'invalid':"Ingrese un código postal válido.", 'min_value':'Ingrese un código de 4 caracteres.'})
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
	dia = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,32)],label="Día")


class CustomerEditForm(ModelForm):
	class Meta:
		model = Customer
		fields = ["nombre",
				 "apellido",
				 "tel",
				 "direccion",
				 "code_postal",
				 "estado_civil",
				 "religion",
		]

	def __init__(self, *args, **kwargs):
		super(CustomerEditForm, self).__init__(*args, **kwargs)
		self.fields['tel'].widget =forms.NumberInput(attrs={'maxlength':14})
		self.fields['code_postal'].widget =forms.NumberInput(attrs={'maxlength':4})

class CustomerDateEditForm(CustomerEditForm):
	ano = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1970,2015)], label="Año")
	mes = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,13)])
	dia = forms.ChoiceField(choices=[(str(i),str(i)) for i in range(1,32)],label="Día")

class UuidForm(forms.Form):	
	uuid = forms.CharField(widget = forms.HiddenInput(), required = False)




class ResetEmailForm(forms.Form):
	email = forms.EmailField(label='Correo Electrónico')

	def clean(self):
		cleaned_data = super(ResetEmailForm, self).clean()

		email = cleaned_data.get("email")
		if not Customer.objects.filter(email=email).exists():
			raise forms.ValidationError("No existe un usuario con este email.")
		return cleaned_data


class PremiumForm(CustomerForm):
	tarjeta_credito = forms.CharField()
	tipo_tarjeta = forms.ChoiceField(choices=TIPOS_TARJETAS)
	fecha_venc_tarjeta = forms.DateField()
	codigo_seguridad = forms.IntegerField(error_messages={'invalid':"Ingrese un código postal valido."})




