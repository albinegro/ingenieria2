from django.contrib import admin
from .models import *
# Register your models here.


class ReservaAdmin(admin.ModelAdmin):
    model = Reserva

admin.site.register(Reserva, ReservaAdmin)