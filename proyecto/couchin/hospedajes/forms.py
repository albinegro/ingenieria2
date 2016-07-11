# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import TipoHospedaje, Hospedaje, Preguntar
from django import forms

class HospedajeForm(ModelForm):
	titulo = forms.CharField(label="Título")
	descripcion = forms.CharField(label="Descripción")
	direccion = forms.CharField(label="Dirección")
	class Meta:
	    model= Hospedaje
	    exclude = ['customer', 'estado', 'favoritos']

	    def __init__(self, *args, **kwargs):
			super(HospedajeForm, self).__init__(*args, **kwargs)
			self.fields['capacidad'].widget =forms.NumberInput(attrs={'min':0})

class FotoForm(HospedajeForm):
	foto_1 = forms.ImageField(required=False)
	foto_2 = forms.ImageField(required=False)
	foto_3 = forms.ImageField(required=False)
	foto_4 = forms.ImageField(required=False)
	foto_5 = forms.ImageField(required=False)

class TipoHospedajeForm(ModelForm):
	class Meta:
		model = TipoHospedaje
		exclude = ['activo']
		
	def clean(self):

		cleaned_data = super(TipoHospedajeForm, self).clean()

		descripcion = cleaned_data.get("descripcion")
		string = descripcion.upper()
		for tipo in TipoHospedaje.objects.all():
			if string == tipo.descripcion.upper():
			    raise forms.ValidationError("Ya existe este tipo de hospedaje.")
		if TipoHospedaje.objects.filter(descripcion=descripcion).exists():
			raise forms.ValidationError("Ya existe este tipo de hospedaje.")
		return cleaned_data


class PreguntarForm(ModelForm):
	class Meta:
		model = Preguntar
		fields = ['pregunta']


class PreguntarEditForm(ModelForm):
	class Meta:
		model = Preguntar
		fields = ['respuesta']


