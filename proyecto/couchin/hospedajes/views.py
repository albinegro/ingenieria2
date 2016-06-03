from django.shortcuts import redirect, get_object_or_404, render
from .forms import TipoHospedajeForm
from .models import TipoHospedaje
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from core.libs import check_temporal, check_admin
# Create your views here.


@user_passes_test(check_temporal)
def view_detail(request):
	return render(request, "hospedaje/view_details.html")


@user_passes_test(check_temporal)
def list_couchin(request):
	return render(request, "hospedaje/list_counchin.html")


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
		tipo.delete() 
		return redirect(reverse('home:close_popup'))
	else:
		if tipo.activo:
			html = "admin/confirm_delete.html"
		else:
			html = "admin/confirm_update.html"
	return render(request, html)
