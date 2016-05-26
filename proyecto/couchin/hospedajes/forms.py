from django.forms import ModelForm
from .models import TipoHospedaje
from django import forms

class TipoHospedajeForm(ModelForm):
	class Meta(object):
		model = TipoHospedaje
		exclude = ['activo']
		
	def clean(self):

		cleaned_data = super(TipoHospedajeForm, self).clean()

		descripcion = cleaned_data.get("descripcion")
		if TipoHospedaje.objects.filter(descripcion=descripcion).exists():
			raise forms.ValidationError("Ya existe este tipo de hospedaje.")
		return cleaned_data



