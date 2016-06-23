from django.shortcuts import redirect, get_object_or_404, render
from .forms import TipoHospedajeForm, HospedajeForm
from .models import TipoHospedaje, Hospedaje
from customers.models import Customer
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from core.libs import check_admin
# Create your views here.
def delete_hospedaje(request, hospe_id):
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	if request.method == 'POST':
		#if hospedaje.reservas_set.all().exists():
		#	hospedaje.estado = False
		#	hospedaje.save()
		
		hospedaje.delete()
		return redirect(reverse("hospedajes:my_hospedajes",kwargs={"user_id":request.user.id}))

	return render(request, "admin/confirm_delete.html")


def edit_hospedaje(request,hospe_id):
	hospedaje = get_object_or_404(Hospedaje, id=hospe_id)
	if request.method == 'POST':
		form = HospedajeForm(data=request.POST, instance=hospedaje)
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
	return render(request, "hospedaje/view_details.html",{"hospedaje": hospedaje})


def list_couchin(request):
	try:
		if request.user.temp_pass:
			logout(request)
			return redirect(reverse("customers:login"))
	except Exception:
		pass

	return render(request, "hospedaje/list_counchin.html",{"hospedajes":Hospedaje.objects.all()})


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
