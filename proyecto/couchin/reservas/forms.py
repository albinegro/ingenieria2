# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Reserva, Calificacion



class ReservaForm(ModelForm):
	fecha_desde = forms.DateField(error_messages={'invalid':"Rango de fecha invalido"})
	fecha_hasta = forms.DateField(error_messages={'invalid':"Rango de fecha invalido"})
	class Meta:
		model = Reserva
		exclude = ["hospedaje", "inquilino", "dueno", "estado", "visto"]

	def clean(self):
		cleaned_data = super(ReservaForm, self).clean()
		
		hasta = cleaned_data.get("fecha_hasta")
		desde = cleaned_data.get("fecha_desde")
		if not desde or not hasta:
			raise forms.ValidationError("Datos requeridos", code="required")
		for reserva in Reserva.objects.filter(estado="aceptada"):
			if reserva.hospedaje.estado:
				if ((reserva.fecha_desde< desde < reserva.fecha_hasta ) or
						(reserva.fecha_desde < hasta < reserva.fecha_hasta) or
							(desde < reserva.fecha_desde < hasta) or 
								(desde < reserva.fecha_hasta < hasta) or
									(reserva.fecha_desde == desde ) or 
										(reserva.fecha_hasta == hasta)):
					
					
					raise forms.ValidationError("Este rango de fechas ya esta reservada.", code="invalid")
		return cleaned_data


class CalificacionForm(ModelForm):
	class Meta:
		model = Calificacion
		exclude = []



