from django.contrib import admin
from .models import *
# Register your models here.


class HospedajeAdmin(admin.ModelAdmin):
    model = Hospedaje

admin.site.register(Hospedaje, HospedajeAdmin)

class TipoHospedajeAdmin(admin.ModelAdmin):
    model = TipoHospedaje

admin.site.register(TipoHospedaje, TipoHospedajeAdmin)