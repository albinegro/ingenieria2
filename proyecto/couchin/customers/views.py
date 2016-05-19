import datetime
from django.shortcuts import render, redirect
from .models import Tarjeta, Customer
from .forms  import PremiumForm, CustomerForm
from django.core.urlresolvers import reverse


# Create your views here
def select_account(request):
	return render(request, "user/select_account.html")

def create_user_premium(request):
	
	form = PremiumForm(request.POST or None)
	if form.is_valid():
		t = Tarjeta()
		t.tarjeta_credito = form.cleaned_data["tarjeta_credito"]
		t.tipo_tarjeta = form.cleaned_data["tipo_tarjeta"]
		t.fecha_venc_tarjeta = form.cleaned_data["fecha_venc_tarjeta"]
		t.codigo_seguridad = form.cleaned_data["codigo_seguridad"]
		t.save()
		customer = form.save(commit=False)
		customer.tarjeta = t
		customer.premiun = True
		customer.fecha_premium = datetime.datetime.now()
		customer.set_password(form.cleaned_data["password"])
		customer.save()
		return redirect(reverse('home:close_popup'))
	return render(request, "user/create_user.html", {"form":form})



def create_user_client(request):
	form = CustomerForm(request.POST or None)
	if form.is_valid():
		customer = form.save(commit=False)
		customer.cliente = True
		customer.set_password(form.cleaned_data["password"])
		customer.save()

		return redirect(reverse('home:close_popup'))
	return render(request, "user/create_user.html", {"form":form})

