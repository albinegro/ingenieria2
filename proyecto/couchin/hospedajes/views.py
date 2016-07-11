from .forms import TipoHospedajeForm, HospedajeForm, PreguntarForm, PreguntarEditForm
from .models import TipoHospedaje, Hospedaje, Preguntar
from customers.models import Customer
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from core.libs import check_admin
from django.db.models import Q
import datetime


@login_required
def responder(request,pregun_id):
	pregunta = get_object_or_404(Preguntar, id=pregun_id)
	if request.method == 'POST':
		form = PreguntarEditForm(request.POST, instance=pregunta)
		if form.is_valid():
			form.save()
			return redirect(reverse("home:close_popup"))
	else:
		form = PreguntarEditForm(instance=pregunta)
	return render(request, "hospedaje/responder.html", {"form":form})


@login_required
def my_favoritos(request, user_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	customer = get_object_or_404(Customer, id=user_id)
	return render(request,"hospedaje/list_my_favoritos.html",{"favoritos":customer.cus_favo.all()})


# Create your views here.
@login_required
def make_favorito(request, user_id, hospe_id):
	customer = get_object_or_404(Customer,id=user_id)
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	try:
		if  customer in hospedaje.favoritos.all() :
			hospedaje.favoritos.remove(customer)
		else:
			hospedaje.favoritos.add(customer)
	except Exception:
		hospedaje.favoritos.add(customer)
	return redirect(reverse("hospedajes:view_detail",kwargs={"hospe_id":hospedaje.id}))

@login_required
def info_booking(request,hospe_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	hospedaje = get_object_or_404(Hospedaje,id=hospe_id)
	return render(request, "hospedaje/info_booking.html",{'hospedaje': hospedaje})




def delete_hospedaje(request, hospe_id):
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	if request.method == 'POST':
		if hospedaje.imueble.all().exists():
			hospedaje.estado = False
			hospedaje.save()
			for reserva in hospedaje.imueble.filter(estado="pendiente"):
				reserva.estado = "rechazada"
				reserva.save()
		else:
			hospedaje.delete()
		return redirect(reverse("home:close_popup"))

	return render(request, "admin/confirm_delete.html")


def edit_hospedaje(request,hospe_id):
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	if request.method == 'POST':
		form = HospedajeForm(request.POST, request.FILES, instance=hospedaje)
		if form.is_valid():
			form.save()
			return redirect(reverse("hospedajes:my_hospedajes",kwargs={"user_id":request.user.id}))
	else:
		form = HospedajeForm(instance=hospedaje)
	return render(request, "hospedaje/update_couchin.html", {"form":form})


def my_hospedajes(request, user_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	customer = get_object_or_404(Customer, id=user_id)
	return render(request,"hospedaje/list_my_counchin.html",{"hospedajes":Hospedaje.objects.filter(customer=customer)})


@login_required
def list_photo(request, hospe_id):
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	photos = [
			  hospedaje.foto_1,
			  hospedaje.foto_2,
			  hospedaje.foto_3,
			  hospedaje.foto_4,
			  hospedaje.foto_5
	]
	return render(request, "hospedaje/list_photo.html", {
		'photos': photos,
	})

@login_required
def create_hospedaje(request):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	if request.POST:
		form = HospedajeForm(request.POST, request.FILES)
		if form.is_valid():
			hospedaje = form.save(commit=False)
			hospedaje.customer = request.user
			hospedaje.save()

			return redirect(reverse("hospedajes:my_hospedajes",kwargs={"user_id":request.user.id}))
	else:
		form = HospedajeForm()
		form.fields["tipo"].queryset = TipoHospedaje.objects.filter(activo=True)
	return render(request,"hospedaje/create_hospedaje.html",{"form":form})


def view_detail(request, hospe_id):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	if request.method == "POST":
		form = PreguntarForm(request.POST)
		if form.is_valid():
			pregunta = form.save(commit=False)
			pregunta.customer = request.user
			pregunta.hospedaje = hospedaje
			pregunta.save()
			return redirect(reverse('hospedajes:view_detail',kwargs={"hospe_id":hospedaje.id}))
	else:
		form = PreguntarForm()
	all_preguntas = Preguntar.objects.filter(hospedaje=hospedaje)
	return render(request, "hospedaje/view_details.html",{"hospedaje": hospedaje, "form":form, "all_preguntas":all_preguntas})

def list_couchin(request):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass

	hospedaje = Hospedaje.objects.filter(estado=True).exclude(tipo__activo=False)
	if 'search_titulo' in request.GET and request.GET.get('search_titulo'):
		hospedaje = hospedaje.filter(
					Q(titulo__icontains=request.GET.get('search_titulo')) |
					Q(descripcion__icontains=request.GET.get('search_titulo'))

					)
	if 'search_tipo' in request.GET and request.GET.get('search_tipo'):
		hospedaje = hospedaje.filter(tipo__descripcion=request.GET.get('search_tipo'))
	if 'search_capa' in request.GET and request.GET.get('search_capa'):
		hospedaje = hospedaje.filter(capacidad=int(request.GET.get('search_capa')))
	hospe_dates = []
	if 'account_date_0' in request.GET and 'account_date_1' in request.GET and  request.GET.get('account_date_0') and request.GET.get('account_date_1'):
		desde = datetime.datetime.strptime(request.GET.get('account_date_0'), '%Y-%m-%d').date()
		hasta = datetime.datetime.strptime(request.GET.get('account_date_1'), '%Y-%m-%d').date()
		if desde > hasta:
			hasta = datetime.datetime.strptime(request.GET.get('account_date_0'), '%Y-%m-%d').date()
			desde = datetime.datetime.strptime(request.GET.get('account_date_1'), '%Y-%m-%d').date()

		for hospe in hospedaje:
			if hospe.imueble.filter(estado="aceptada").exists():
				for reserva in hospe.imueble.filter(estado="aceptada"):
						if not ((reserva.fecha_desde < desde < reserva.fecha_hasta ) or 
								(reserva.fecha_desde < hasta < reserva.fecha_hasta) or 
									(desde < reserva.fecha_desde < hasta) or 
										(desde < reserva.fecha_hasta < hasta) or
											(reserva.fecha_desde == desde ) or 
												(reserva.fecha_hasta == hasta)):
					
							if hospe not in hospe_dates:
								hospe_dates.append(hospe)
						else:
							try:
								hospe_dates.remove(hospe)
							except Exception:
								pass

							break 
			else:
				hospe_dates.append(hospe)
			
	tipo = TipoHospedaje.objects.filter(activo=True)
	if hospe_dates:
		hospedaje = hospe_dates

	return render(request, "hospedaje/list_counchin.html",{"hospedajes":hospedaje, "tipo":tipo})


@user_passes_test(check_admin)
def list_type(request):
	form = TipoHospedajeForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(reverse('hospedajes:list_type'))
	return render(request, "admin/edit_type.html", {"form":form, "tipos":TipoHospedaje.objects.all()})


@login_required
@user_passes_test(check_admin)
def add_type(request):
	form = TipoHospedajeForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(reverse('home:close_popup'))
	return render(request, "admin/add_type.html", {"form":form, "tipos":TipoHospedaje.objects.all()})


@login_required
@user_passes_test(check_admin)
def edit_type(request,type_id):
	tipo = get_object_or_404(TipoHospedaje, id=type_id)
	if request.method == 'POST':
		form = TipoHospedajeForm(data=request.POST, instance=tipo)
		if form.is_valid():
			form.save()
			return redirect(reverse('home:close_popup'))
	else:
		form = TipoHospedajeForm(instance=tipo)
	return render(request, "admin/update_type.html", {"form":form})


@login_required
@user_passes_test(check_admin)
def delete_type(request,type_id):
	tipo = get_object_or_404(TipoHospedaje, id=type_id)
	if request.method == 'POST':
		if tipo.hospedaje_set.exists():
			tipo.activo = not tipo.activo
			tipo.save()
		else:
			tipo.delete() 
		return redirect(reverse('home:close_popup'))
	else:
		if tipo.activo:
			html = "admin/confirm_delete.html"
		else:
			html = "admin/confirm_update.html"
	return render(request, html)
