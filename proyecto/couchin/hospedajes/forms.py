from django.forms import ModelForm
from .models import TipoHospedaje, Hospedaje
from django import forms
from multiupload.fields import MultiFileField

class HospedajeForm(ModelForm):
	class Meta:
	    model= Hospedaje
	    exclude = ['customer', 'estado']

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


