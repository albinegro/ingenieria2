import datetime

from django.shortcuts import render, redirect
from .models import Tarjeta, Customer
from .forms  import TarjetaForm, CustomerForm, CustomerDateForm
from django.core.urlresolvers import reverse


# Create your views here
def select_account(request):
	return render(request, "user/select_account.html")

# Create your views here
def info_account(request,user_id):
	return render(request, "user/info_account.html")

def update_premium(request, user_id):
	form = form = TarjetaForm(request.POST or None)
	if form.is_valid():
		tarjeta = form.save(commit=False)
		tarjeta.premiun_pago = "80"
		tarjeta.save()
		customer = Customer.objetos.get(id=user_id)
		customer.tarjeta = tarjeta
		customer.premium = True
		customer.cliente = False
		customer.save()
		return redirect(reverse('home:home'))
	return render(request, "user/update_premium.html", {"form":form})

def create_user_client(request):
	form = CustomerDateForm(request.POST or None)
	if form.is_valid():
		customer = form.save(commit=False)
		customer.cliente = True
		customer.set_password(form.cleaned_data["password"])
		customer.fecha_n = datetime.datetime(int(form.cleaned_data["ano"]), 
			                                 int(form.cleaned_data["mes"]),
			                                 int(form.cleaned_data["dia"]))
		customer.save()

		return redirect(reverse('home:home'))
	return render(request, "user/create_user.html", {"form":form})


def admin_conf(request):
	return render(request, "admin/menu_admin.html")



