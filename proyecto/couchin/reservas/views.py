import datetime
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from hospedajes.models import Hospedaje
from customers.models import Customer
from .forms import *
from .models import Reserva

@login_required
def view_calificacion(request, cali_id):
	cali = get_object_or_404(Calificacion, id=cali_id)
	return render(request, "calificacion/view_cali.html",{"cali":cali})

@login_required
def make_calificacion_inquilino(request, reserva_id):
	reserva = get_object_or_404(Reserva, id=reserva_id)
	if request.method == "POST":
		form = CalificacionForm(request.POST)
		if form.is_valid():
			cali = form.save(commit=False)
			cali.save()
			reserva.califica_inquilino = cali
			reserva.save()
			return redirect(reverse("home:close_popup"))
	else:
		form = CalificacionForm()
	return render(request,"calificacion/make_cali.html",{"form":form})


@login_required
def make_calificacion_dueno(request, reserva_id):
	reserva = get_object_or_404(Reserva, id=reserva_id)
	if request.method == "POST":
		form = CalificacionForm(request.POST)
		if form.is_valid():
			cali = form.save(commit=False)
			cali.save()
			reserva.califica_dueno = cali
			reserva.save()
			return redirect(reverse("home:close_popup"))
	else:
		form = CalificacionForm()
	return render(request,"calificacion/make_cali.html",{"form":form})



@login_required
def post_acept(request):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	return render(request,"reservas/post_acept.html")

@login_required
def acept_reserva(request, hospe_id, rese_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	reserva = get_object_or_404(Reserva, id=rese_id)
	if request.method == 'POST':
		reserva.estado = "aceptada"
		reserva.save()
		for rese in hospedaje.imueble.filter(estado="pendiente"):
			if ((reserva.fecha_desde < rese.fecha_desde < reserva.fecha_hasta ) or 
					(reserva.fecha_desde < rese.fecha_hasta < reserva.fecha_hasta) or 
						(rese.fecha_desde < reserva.fecha_desde < rese.fecha_hasta) or 
							(rese.fecha_desde < reserva.fecha_hasta < rese.fecha_hasta) or
								(reserva.fecha_desde == rese.fecha_desde ) or 
									(reserva.fecha_hasta == rese.fecha_hata)):
				rese.estado = "rechazada"
				rese.save()
		return redirect(reverse("home:close_popup"))
	return render(request,"reservas/acept_reserva.html")
		

# Create your views here.
def perdelta(start, end, delta):
	curr = start
	while curr < end:
		yield curr
		curr += delta


@login_required
def make_booking(request, hospe_id, user_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	customer = get_object_or_404(Customer, id=user_id)
	if request.method == 'POST':
		form = ReservaForm(request.POST,{"hospedaje":hospe_id})
		if form.is_valid():
			reserva = form.save(commit=False)
			if form.cleaned_data.get("fecha_desde") > form.cleaned_data.get("fecha_hasta"):
				reserva.fecha_desde = form.cleaned_data.get("fecha_hasta")
				reserva.fecha_hasta = form.cleaned_data.get("fecha_desde")
			reserva.inquilino = customer
			reserva.dueno = hospedaje.customer
			reserva.hospedaje = hospedaje
			reserva.save()
			return redirect(reverse("reservas:post_acept"))
	else:
		form = ReservaForm()
	if form.errors:
		if form.errors.get('__all__')[0] == 'Este rango de fechas ya esta reservada.':
			form.errors["fecha_desde"] = ['Este rango de fechas ya esta reservado.']
			form.errors["fecha_hasta"] = ['Este rango de fechas ya esta reservado.']
	re = []
	for hospe in hospedaje.imueble.filter(estado="aceptada"):
		for result in perdelta(hospe.fecha_desde, hospe.fecha_hasta, timedelta(days=1)):
			re.append(result.isoformat())
	return render(request,"reservas/booking.html",{"form":form, "reservas":re, "hosid":hospe_id})


def my_booking(request, user_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	customer = get_object_or_404(Customer, id=user_id)

	return render(request,"reservas/my_list_booking.html",{"reservas":Reserva.objects.filter(inquilino=customer).order_by("-fecha_desde").order_by("-hospedaje__titulo")})


def my_rental(request, user_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	customer = get_object_or_404(Customer, id=user_id)
	reservas = Reserva.objects.filter(dueno=customer,).exclude(estado="rechazada").order_by("-fecha_desde").order_by("-hospedaje__titulo")
	if 'account_date_0' in request.GET and 'account_date_1' in request.GET and  request.GET.get('account_date_0') and request.GET.get('account_date_1'):
		desde = datetime.strptime(request.GET.get('account_date_0'), '%Y-%m-%d').date()
		hasta = datetime.strptime(request.GET.get('account_date_1'), '%Y-%m-%d').date()
		if desde > hasta:
			hasta = datetime.strptime(request.GET.get('account_date_0'), '%Y-%m-%d').date()
			desde = datetime.strptime(request.GET.get('account_date_1'), '%Y-%m-%d').date()
		reservas = reservas.filter(fecha_desde__range=(desde,hasta),fecha_hasta__range=(desde,hasta))


	return render(request,"reservas/my_list_rental.html",{"reservas":reservas})